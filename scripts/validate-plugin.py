"""Validate this plugin's package and agent contracts; does not run Copilot."""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


EXPECTED = {
    "angular-bootstrap-italia-orchestrator": (
        "Angular Bootstrap Italia Orchestrator",
        {"angular-developer", "angular-bootstrap-italia", "modern-css", "web-typography"},
    ),
    "angular-architect": ("Angular Architect", {"angular-developer"}),
    "bootstrap-italia-specialist": ("Bootstrap Italia Specialist", {"angular-bootstrap-italia"}),
    "scss-specialist": ("SCSS Specialist", {"modern-css", "web-typography"}),
}
SKILLS = {"angular-developer", "angular-bootstrap-italia", "modern-css",
          "web-typography", "ponytail", "caveman"}
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently accepting the last value."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("Missing YAML frontmatter")
    data = yaml.load(match[1], Loader=UniqueLoader)
    if not isinstance(data, dict):
        raise ValueError("Frontmatter must be a mapping")
    for field in ("name", "description"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f"Missing/non-string {field}")
    return data, text[match.end():]


def local_links(path, root):
    # Validate inline Markdown file links outside code fences. URL/anchor checks
    # require network/rendering and are deliberately outside this static check.
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$", "", text)
    for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
        target = target.strip().strip("<>")
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        resolved = (path.parent / unquote(parts.path)).resolve()
        if not resolved.is_relative_to(root):
            raise ValueError(f"Link escapes package: {target}")
        if not resolved.exists():
            raise ValueError(f"Missing link target: {target}")
        yield resolved


def validate(root):
    root = root.resolve()
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    try:
        manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
        require(manifest.get("$schema") == SCHEMA, "Incorrect Agent Plugins 1.0 schema")
        name = manifest.get("name", "")
        require(isinstance(name, str) and bool(re.fullmatch(r"[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?", name))
                and "--" not in name and ".." not in name, "Invalid plugin name")
        allowed = {"$schema", "name", "version", "description", "author", "license",
                   "keywords", "homepage", "repository", "extensions"}
        require(not set(manifest) - allowed, "Unsupported top-level manifest fields")
        require(bool(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", ""))),
                "This package requires a numeric major.minor.patch version")
    except (OSError, ValueError, TypeError, AttributeError) as error:
        errors.append(f"plugin.json: {error}")

    agents_dir = root / "com.github.copilot/agents"
    actual = {p.name.removesuffix(".agent.md") for p in agents_dir.glob("*.agent.md")}
    require(actual == set(EXPECTED), "Agent file inventory does not match the four-agent contract")
    names = []
    roots = [root / "README.md", root / "com.github.copilot/execution-contract.md"]
    for stem, (expected_name, domain_skills) in EXPECTED.items():
        path = agents_dir / f"{stem}.agent.md"
        roots.append(path)
        try:
            data, body = frontmatter(path)
            names.append(data["name"])
            require(data["name"] == expected_name, f"{path.name}: incorrect agent identity")
            require(len(body) <= 30000, f"{path.name}: agent body exceeds 30,000 characters")
            parent = stem == "angular-bootstrap-italia-orchestrator"
            require(data.get("user-invocable") is parent, f"{path.name}: wrong user-invocable")
            require(data.get("disable-model-invocation") is parent,
                    f"{path.name}: wrong disable-model-invocation")
            expected_agents = [v[0] for k, v in EXPECTED.items() if k != stem] if parent else []
            require(data.get("agents") == expected_agents, f"{path.name}: invalid delegation allowlist")
            tools = data.get("tools")
            expected_tools = {"read", "search", "web"} | (
                {"agent", "edit", "execute", "browser", "todo"} if parent else set())
            require(isinstance(tools, list) and all(isinstance(t, str) for t in tools)
                    and set(tools) == expected_tools, f"{path.name}: unexpected/missing tool permissions")
            links = set(local_links(path, root))
            require((root / "com.github.copilot/execution-contract.md") in links,
                    f"{path.name}: missing execution contract link")
            for skill in domain_skills | {"ponytail", "caveman"}:
                require(root / "skills" / skill / "SKILL.md" in links,
                        f"{path.name}: missing bundled skill link: {skill}")
                if not parent and skill in domain_skills:
                    require(f"Required skill used: {skill}" in body,
                            f"{path.name}: missing domain completion marker: {skill}")
            require("Task status: FAILED" in body, f"{path.name}: missing explicit failure rule")
        except (OSError, ValueError, TypeError, yaml.YAMLError) as error:
            errors.append(f"{path.name}: {error}")
    require(len(names) == len(set(names)), "Duplicate agent names")

    skills_dir = root / "skills"
    require({p.parent.name for p in skills_dir.glob("*/SKILL.md")} == SKILLS,
            "Bundled skill inventory does not match the six-skill contract")
    for skill in sorted(SKILLS):
        path = skills_dir / skill / "SKILL.md"
        roots.append(path)
        try:
            data, _ = frontmatter(path)
            require(data["name"] == skill, f"{path}: skill name/directory mismatch")
        except (OSError, ValueError, TypeError, yaml.YAMLError) as error:
            errors.append(f"{path}: {error}")
    for directory in (skills_dir, root / "com.github.copilot"):
        require(not any(directory.rglob(".git")), f"Copied Git metadata inside {directory.name}")

    visited = set()
    while roots:
        path = roots.pop().resolve()
        if path in visited:
            continue
        visited.add(path)
        try:
            require(path.stat().st_size > 0, f"Empty required/referenced file: {path}")
            roots.extend(p for p in local_links(path, root) if p.suffix.lower() == ".md")
        except (OSError, ValueError) as error:
            errors.append(f"{path.relative_to(root)}: {error}")
    return errors, len(visited)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, documents = validate(args.root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"PASS: 4 agents, 6 skills, {documents} linked Markdown documents; static checks only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
