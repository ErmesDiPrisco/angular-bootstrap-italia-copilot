# Mandatory execution contract

This contract applies to the orchestrator and every specialist. Read it before
domain analysis. It defines acceptance of work, not a runtime security boundary.

## Load the actual bundled skills

1. Read every `SKILL.md` linked in your agent's Mandatory startup section in the
   current invocation. A name, description, activation marker, parent summary
   or earlier subagent invocation is not the skill's full instructions.
2. Resolve links relative to the agent file inside the installed plugin. The
   plugin's `skills/` folder is distinct from the target application's root.
   Use the exact bundled files, not same-named skills from other plugins or
   `external/`. Do not assume the current working directory is the plugin root.
3. If automatic skill loading supplies the complete matching file, use it;
   otherwise open it with a file-reading tool. Read task-relevant references
   relative to that skill's directory. Never claim a file was read if access
   failed or only search snippets were returned.
4. Apply Ponytail in Full mode and Caveman in Ultra mode from their actual
   instructions. Slash commands are user-facing conveniences, not shell
   commands or evidence of activation. Writing `/ponytail` or `/caveman ultra`
   in a response does not load a skill.
5. Record the resolved file, relevant section/reference and a concrete
   task-specific application for every required skill, including cross-cutting
   skills. For a review, cite a finding or a checked design choice. Do not
   fabricate applications or compress away this evidence.

If a required skill or necessary reference is unavailable, unread or unused,
stop that subtask. Do not substitute model knowledge or print success markers.

## Scope and precedence

Follow platform instructions and explicit user requirements. Within this plugin:

1. Preserve the requested Bootstrap Italia foundation and verified public
   contracts, installed-version compatibility, Angular correctness and
   accessibility. These are concurrent requirements, not tradeoffs.
2. Apply domain skills within the specialist's responsibility and existing
   project conventions. Resolve disagreements using inspected evidence.
3. Apply Ponytail to remove unnecessary code, not required features, tests,
   cleanup, evidence or documentation.
4. Apply Caveman to conversational style, not code, UI copy, comments, commits,
   documentation or evidence fields. Preserve the user's language and full
   technical meaning. Honor explicit style overrides and report them instead
   of falsely claiming an active mode.

The specific angular-bootstrap-italia restrictions prevail over modern-css's
generic library replacement recipes, global resets, mandatory new themes and
Ponytail's preference for native replacements. Skill use means understanding and
applying it in scope, not blindly copying every example. State scoped exceptions.
Angular guidance must match installed APIs and the current angular-developer
forms policy; do not enforce Reactive Forms regardless of version and context.

`refactoring-ui` and `top-design`, mentioned as related reading by
web-typography, are not bundled or mandatory dependencies. Do not pretend they
were loaded. Use the bundled typography guidance and verified project design
system; request additional skills only for explicitly expanded scope.

## Delegation and evidence

The orchestrator must call the named custom agents through the host's subagent
tool. Writing an agent name, using a handoff, or assigning a generic agent the
same role is not equivalent. If the host cannot invoke a required custom agent,
fail with `AGENT_UNAVAILABLE`; never silently perform its work in the parent.

Each delegated request must provide the task ID, analysis or review phase,
original requirements, target application path, resolved plugin/skill paths,
versions and their evidence, relevant files, constraints, dependencies and
acceptance checks. Subagents do not automatically inherit the parent's skills
or earlier specialist results. Pass accepted reports explicitly when needed.

Specialists are read-only. They report proposed commands and checks; only the
orchestrator edits application files or executes build/test commands. Web access
is research, not permission to send project code or secrets to external sites.
Use official sources and distinguish documentation, source observations,
inferences and executed checks. Uncertainty must remain visible.

Every specialist response starts with:

```text
Task ID: <delegated ID>
Phase: ANALYSIS | REVIEW
Agent: <exact agent name>
Task status: PASSED | FAILED
```

Choose one value per field. Then include `Skill evidence` with one row per
required skill: skill name, resolved path, section/references read, and concrete
application. Include findings, inspected versions/files, constraints, proposed
checks, and checks actually observed. `PASSED` means this analysis/review met its
contract; it does not mean the implementation has passed builds or browser tests.
On success, append the markers defined by the agent. Markers alone are insufficient.
If the user explicitly overrides a cross-cutting mode, replace its active-mode
claim with the actual override while retaining evidence that the skill was read
and its applicable rules respected. Never waive a missing or unread skill.

On failure, return the header with `Task status: FAILED`, followed by:

```text
Failure code: <code>
Missing or unused requirement: <skill, reference, agent, context or check>
Evidence: <attempted path/tool and actual result>
Impact: <work that cannot proceed>
Recovery: <specific correction needed>
```

Use `SKILL_UNAVAILABLE`, `SKILL_NOT_USED`, `REFERENCE_UNAVAILABLE`,
`AGENT_UNAVAILABLE`, `MISSING_REQUIRED_CONTEXT`, `PUBLIC_CONTRACT_UNVERIFIED`
or `REVIEW_FAILED` as appropriate. Do not add successful completion markers.

## Acceptance gate

The orchestrator verifies the real agent identity, task/phase, status, all skill
evidence, required markers (or documented explicit mode override) and consistency
with inspected files. Reject missing, contradictory or unsupported reports.
Re-open disputed sources when necessary. Do not accept a generic confirmation
that a skill is active.

A failed attempt remains failed. One corrective re-invocation is allowed when
the missing file/context/tool has been restored or the specialist can perform
the omitted reading/application. Require a complete new analysis; adding markers
to the old response is not remediation. If the corrected attempt still fails,
report overall `Task status: FAILED` and the failure code. No indefinite retries,
implementation dependent on rejected advice, or success after a missing skill.

Prompt instructions and self-reported evidence cannot mathematically prove model
compliance. Preserve host tool traces for review when available; never present
this protocol or the static repository validator as executable runtime enforcement.
