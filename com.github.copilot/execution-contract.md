# Execution contract

Shared rules for the orchestrator and specialists. Read before domain work;
reuse unchanged full content already in the current context. These instructions
define acceptance, not an executable runtime enforcement boundary.

## Mandatory skills and evidence

- Load and apply every skill assigned by the agent file. The orchestrator's
  domain skills are conditional on routing; each invoked specialist uses all
  its assigned skills. SIMPLE_FIX does not waive any skill obligation.
- Resolve exact bundled files relative to the installed agent file, separately
  from the target application. Do not substitute external/ or another plugin.
- Reuse a complete, matching, unchanged SKILL.md already in this agent context;
  otherwise read it. Reload after changes, uncertain identity/freshness or loss
  of full content. A fresh subagent must load its own skills; another agent's
  summary, search snippets, slash commands or activation markers do not suffice.
- Read only task-relevant linked references, resolving from the skill directory.
  Reuse full unchanged references under the same rules. Do not claim failed
  reads as successful or replace missing required guidance with model knowledge.
- Apply Ponytail Full and Caveman Ultra. For every required skill, record its
  resolved path, relevant section/reference and a concrete task-specific decision
  or reviewed finding. Keep evidence concise, not just an activation claim.

An unavailable, unread or unused required skill/reference fails that subtask.
Stop dependent work; do not return success markers.

## Precedence and boundaries

Follow platform instructions and explicit user requirements. Preserve installed
version compatibility, Angular correctness, accessibility and verified public
Bootstrap Italia contracts together. Follow valid project conventions.

- Bootstrap Italia is immutable: no dependency/source/compiled-asset edits,
  patch-package, post-install mutations, monkey patches, private overrides or
  copied-and-modified internals. Source inspection is read-only; a reachable
  export or typings member alone does not establish a supported public API.
- Its specific skill restrictions override modern-css/native replacement,
  global reset and new-theme recipes. Do not replace its core behavior or use
  another UI library as a shortcut. Document applicable scoped exceptions.
- Ponytail removes unnecessary code, not requested features, cleanup, tests or
  evidence. Caveman changes conversational style, not code, UI copy, comments,
  commits or documentation. Preserve the user's language and technical meaning.
  Record explicit user mode overrides instead of claiming an inactive mode.
- Angular forms guidance must match installed APIs and the domain skill; do not
  force Reactive Forms or unrequested migrations.
- Typography's related refactoring-ui and top-design are not bundled or
  mandatory. Do not claim to load them or request them without expanded scope.

## Workflow selection

The orchestrator records `Workflow: SIMPLE_FIX | STANDARD` with a brief reason
after inspecting the affected code. Routing selects domains; workflow selects
whether those domains need design analysis before implementation.

Use SIMPLE_FIX only when **all** these conditions hold:

1. An existing implementation has a clearly identified cause and an observable
   expected result; the correction is local and involves exactly one domain.
2. Existing design, public APIs, shared-consumer contracts and verified library
   boundaries remain unchanged. No component creation, replacement, extension,
   architectural choice, dependency/configuration change or uncertain public API.
3. No change to lifecycle, asynchronous ownership/cancellation, SSR/hydration,
   security/permissions, persistence/data contracts or accessibility behavior
   (including semantics, keyboard, focus and ARIA).
4. The orchestrator can name the affected checks, inspect relevant consumers and
   justify that other domains are unaffected using code evidence. Small diff
   size or an unavailable specialist is never evidence of simplicity.

SIMPLE_FIX: inspect and load required skills -> implement -> run relevant checks
-> one required specialist REVIEW of the actual result. There is no mandatory
pre-implementation specialist ANALYSIS. The reviewer checks the original
requirements, simplicity criteria, diff and results directly; an earlier design
report is neither required nor invented. A clean result needs one specialist
invocation; defects can require focused follow-up reviews.

STANDARD: obtain accepted ANALYSIS from affected specialists before dependent
implementation -> implement -> checks -> required implementation REVIEWs.
Resolve component reuse and Bootstrap Italia feasibility before dependent edits.
Analysis-only requests use applicable ANALYSIS calls without edits or invented
implementation reviews. Setup/status questions need no development workflow.

If SIMPLE_FIX assumptions fail, stop dependent edits and switch to STANDARD.
A specialist returns FAILED with `WORKFLOW_ESCALATION_REQUIRED` for newly found
complexity within the selected domain, or `SCOPE_EXPANSION_REQUIRED` for a new
domain, naming the concrete files/contracts and needed expertise. Obtain the
affected design analysis, reconcile any provisional edits, then validate/review
the resulting work. Neither code is accepted nor unrelated specialists invoked
merely because escalation occurred. Unaffected accepted reviews remain valid.

## Delegation

Invoke only affected, named custom agents through the host's subagent tool.
Handoffs, printed names and generic agents assigned a role are not substitutes.
An unavailable required custom agent fails with `AGENT_UNAVAILABLE`; do not
silently take over its review or reclassify its domain as irrelevant.

Send a compact packet: task ID, phase, workflow and reason, user requirements,
application/plugin/skill paths, relevant versions with evidence, affected files
or diff, routing, constraints and acceptance checks. Include reuse candidates
and accepted dependency reports only when relevant. A fresh reviewer needs
enough context to judge the change without the parent's conversation history.

Specialists only read, research and report; the orchestrator alone edits and
executes commands. Distinguish proposed checks from observed results. Use
official sources for external research; distinguish documentation, inspected
source, inference and executed evidence. Do not send project code/secrets to
external sites. Inspect relevant code and necessary dependencies, not the whole
application by default. Reopen disputed or stale evidence when needed.

## Validation and incremental corrections

Before implementation, define observable acceptance criteria and a short check
plan based on actual impact. Keep any checks required by applicable skills,
including the Angular build for Angular code changes. Missing runtime/visual
capability never turns a required check into an optional one. Run checks after
a coherent set of changes; avoid a separate type check when the build already
covers it unless the project requires one.

Keep a compact task-context record of accepted reviews/checks: scope, inspected
revision/diff, dependencies and result. No project bookkeeping files required.

For each correction:

1. Route by the defect's cause and effects, not the original specialist list,
   file extension or whoever reported it. Reinvoke only invalidated domains and
   newly required expertise. Repeat analysis only for changed design/unresolved
   contracts or workflow escalation.
2. Pass the finding, incremental diff, retained constraints and relevant results.
   Retain unaffected accepted reviews with a short justification; no renewal
   calls or duplicate reports. Analysis-only, failed or pending reviews do not
   count as implementation approval. Complete each pending required review once.
3. Reuse passed checks only while relevant inputs/environment remain unchanged
   and no finding challenges them. Run missing checks and rerun failed or
   invalidated ones. Compiled-input changes, including SCSS, invalidate the
   application build; a rebuild alone does not require an Angular reviewer.
4. Stop when all applicable reviews/checks are valid. Do not rerun for reassurance.
   When an attempt makes no progress, diagnose the blocker instead of cycling
   without new evidence. Report unresolved failure/blockage honestly.

| Correction, other contracts unchanged | Review again |
| --- | --- |
| Angular calculation/state/service logic | Angular Architect |
| Bootstrap Italia public option | Bootstrap Italia Specialist |
| Application-owned CSS/SCSS spacing | SCSS Specialist |
| Angular lifecycle interacting with library disposal | Angular Architect + Bootstrap Italia Specialist |

Each reinvoked specialist still applies all assigned skills. Reuse skill content
only under the context rules above. Previously accepted evidence can be cited
briefly when available, with the correction-specific application; do not repeat
the full unchanged report. Retained approval is not a new invocation.

## Compact specialist report

Every response starts with one value per field:

```text
Task ID: <delegated ID>
Phase: ANALYSIS | REVIEW
Agent: <exact custom-agent name>
Task status: PASSED | FAILED
```

Then include:

- `Skill evidence`: one compact row per assigned skill (resolved file,
  section/references, concrete application). No omitted mandatory skill.
- `Findings`: inspected files/versions and evidence, decision or defects with
  file/line references, applicable constraints and dependencies. Omit unrelated
  domain headings; do not fill a full architecture template for a local fix.
- `Validation`: relevant proposed checks versus actual supplied/observed results,
  including missing evidence. Do not claim unexecuted checks passed.

A REVIEW inspects the actual changed files against requirements and supplied
results, plus the accepted design for STANDARD or simplicity criteria for
SIMPLE_FIX. A plan is not implementation approval. Return `REVIEW_FAILED` for
unresolved defects. PASSED certifies only this analysis/review's scope, never
unobserved builds or browser checks. Append the agent's success markers only on
success; document explicit user mode overrides in place of false mode claims.

On failure append, without success markers:

```text
Failure code: <code>
Missing or unused requirement: <skill, reference, agent, context or check>
Evidence: <actual attempted path/tool result or concrete finding>
Impact: <dependent work that cannot proceed>
Recovery: <specific correction needed>
```

Codes: `SKILL_UNAVAILABLE`, `SKILL_NOT_USED`, `REFERENCE_UNAVAILABLE`,
`AGENT_UNAVAILABLE`, `MISSING_REQUIRED_CONTEXT`, `PUBLIC_CONTRACT_UNVERIFIED`,
`WORKFLOW_ESCALATION_REQUIRED`, `SCOPE_EXPANSION_REQUIRED`, `REVIEW_FAILED`.

## Acceptance and recovery

The orchestrator verifies agent identity, task/phase, status, every skill's
evidence, success markers (or explicit override) and consistency with inspected
files. Reject unsupported, missing or contradictory reports.

A failed compliance attempt remains failed. Allow one corrective invocation
after restoring missing access/context or enabling omitted skill reading/use;
require a complete compliant replacement report from that specialist, not added
markers. If it fails again, the task fails. This does not reopen other domains.
Code defects and workflow/scope escalation follow the incremental rules instead.
No dependent implementation on rejected advice or success with missing skills.

Overall completion requires every applicable implementation review and check.
An unsupported request, failed check/review or skill/agent violation is FAILED;
a missing execution environment or necessary product decision is BLOCKED, with
the exact missing input/check. Distinguish implemented code from verified
completion. Preserve host tool traces when available: self-reports and static
package tests do not prove runtime compliance.
