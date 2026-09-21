# Mandatory execution contract

This contract applies to the orchestrator and every specialist. Read it before
domain analysis. It defines acceptance of work, not a runtime security boundary.

## Load the actual bundled skills

1. Before domain work, ensure the full content of every required `SKILL.md` is
   available in your current agent context and apply it. The orchestrator selects
   its conditional domain skills using its routing rules; each invoked specialist
   uses all skills assigned to it. A name, description, activation marker or
   parent summary is not the skill's full instructions.
2. Resolve links relative to the agent file inside the installed plugin. The
   plugin's `skills/` folder is distinct from the target application's root.
   Use the exact bundled files, not same-named skills from other plugins or
   `external/`. Do not assume the current working directory is the plugin root.
3. If automatic skill loading or an earlier read in this same context supplies
   the complete matching, unchanged file, reuse it without another read. Otherwise
   open it with a file-reading tool. Read only task-relevant references, resolving
   them relative to that skill's directory, and reuse unchanged full references
   already available in this context. Reload if the file changed, its identity or
   freshness is uncertain, or its full content is no longer available after
   context loss. A new subagent context must load its own required content;
   another agent's reading or a summary does not satisfy this obligation. Never
   claim a file was read if access failed or only search snippets were returned.
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

The orchestrator determines which specialist domains are affected before
delegating. A skipped, inapplicable specialist needs a reason in the routing
decision, not a call, report, skill load or success marker. This applies to both
analysis and final review. Agent availability must never determine applicability.
All skill obligations remain binding for each selected specialist. A package
validation still requires all six bundled skills even if one task uses fewer.

Route each correction separately from the overall task. A specialist's earlier
participation does not automatically make it necessary for every later defect.
Follow the incremental review rules below; do not restart the full agent workflow
because a single domain failed review.

The orchestrator must call the named custom agents through the host's subagent
tool. Writing an agent name, using a handoff, or assigning a generic agent the
same role is not equivalent. If the host cannot invoke a required custom agent,
fail with `AGENT_UNAVAILABLE`; never silently perform its work in the parent.

Each delegated request must provide the task ID, analysis or review phase,
original requirements, target application path, resolved plugin/skill paths,
versions and their evidence, relevant files, constraints, dependencies and
acceptance checks, plus the routing decision and reuse candidates where relevant.
Subagents do not automatically inherit the parent's skills
or earlier specialist results. Pass accepted reports explicitly when needed.

Specialists are read-only. They report proposed commands and checks; only the
orchestrator edits application files or executes build/test commands. Web access
is research, not permission to send project code or secrets to external sites.
Use official sources and distinguish documentation, source observations,
inferences and executed checks. Uncertainty must remain visible.

If analysis or review uncovers a previously excluded domain, return
`Task status: FAILED`, `Failure code: SCOPE_EXPANSION_REQUIRED`, the affected
files/contracts and the specific additional expertise needed. The orchestrator
must update routing, obtain the newly required analysis and resume the affected
work only after acceptance. This is a changed scope, not a missing-skill retry;
it does not waive the skill failure rule or justify unrelated specialist calls.

## Incremental corrections and validation

The orchestrator keeps a compact record of accepted domain reviews and executed
checks in the task context: scope, inspected revision/diff, result and relevant
dependencies. No new project file or bookkeeping framework is required.

For each defect or correction:

1. Identify the concrete finding, changed behavior/contracts, affected files and
   relevant dependencies since the last accepted review. Route by impact, not
   just extension or the original task's specialist list.
2. Reinvoke only specialists whose conclusions the correction invalidates, plus
   newly required domains. Pass the finding, incremental diff, accepted constraints
   and relevant check results; request a focused review. Repeat design analysis
   only if the fix changes the accepted design or leaves a contract unresolved.
3. Retain accepted reviews for unaffected domains without another call, file read
   or repeated report. Record the basis for retaining them. Never count an
   analysis-only report, failed review, unavailable report or not-yet-performed
   implementation review as accepted. Complete any pending required review once.
4. Reuse successful checks only while their relevant inputs and environment are
   unchanged and no new finding challenges the result. Execute missing checks and
   repeat failed or invalidated checks after a coherent set of corrections. An
   application build is invalidated by changes to compiled inputs, including SCSS;
   rerunning the build does not itself require another Angular specialist call.
5. Stop the correction cycle when the defect is resolved, affected reviews pass
   and all required checks remain valid. Do not request another confirmation from
   every specialist or rerun identical checks for reassurance. An unresolved
   blocker or lack of progress must be reported, not hidden by repeated cycles.

Example: Angular and Bootstrap Italia reviews pass, but SCSS reports incorrect
spacing in an application-owned layout. Correct it and request only SCSS review;
retain the other approvals if their contracts remain unchanged. Rerun affected
style/build/visual checks. If the CSS fix instead affects library-calculated
geometry, add Bootstrap Italia review; add Angular only for a demonstrated
Angular API, binding, template structure, lifecycle or other Angular impact.

The same rule applies symmetrically to every domain, regardless of who found
the defect. A finding raised by one specialist is routed by its actual cause
and effects, not automatically back to all agents or only to the reporting agent.

| Correction with other contracts unchanged | Specialist to invoke again |
| --- | --- |
| Angular calculation, state or service logic; presentation and library integration unchanged | Angular Architect only |
| Bootstrap Italia public option; Angular integration and styling unchanged | Bootstrap Italia Specialist only |
| Application-owned CSS/SCSS spacing; Angular and library contracts unchanged | SCSS Specialist only |
| Angular lifecycle interacting with Bootstrap Italia disposal | Angular Architect and Bootstrap Italia Specialist |

File extension alone does not establish impact. Retain approvals for unchanged
domains in each case; invalidate only conclusions affected by the correction.

Every active specialist still applies all its required skills. When full skill
content and earlier evidence remain available in the same context, cite that
evidence briefly and explain the correction-specific application; do not reload
files or reproduce a full unchanged report just to renew a marker. A fresh agent
context must still load the mandatory content. Retained approval means previously
reviewed, unaffected work; never present it as a new specialist invocation.

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
`AGENT_UNAVAILABLE`, `MISSING_REQUIRED_CONTEXT`, `PUBLIC_CONTRACT_UNVERIFIED`,
`SCOPE_EXPANSION_REQUIRED`
or `REVIEW_FAILED` as appropriate. Do not add successful completion markers.

## Acceptance gate

The orchestrator verifies the real agent identity, task/phase, status, all skill
evidence, required markers (or documented explicit mode override) and consistency
with inspected files. Reject missing, contradictory or unsupported reports.
Re-open disputed sources when necessary. Do not accept a generic confirmation
that a skill is active.

A failed attempt remains failed. One corrective re-invocation is allowed when
the missing file/context/tool has been restored or the specialist can perform
the omitted reading/application. For missing skill use or invalid evidence,
require a complete compliant replacement report from that specialist; adding
markers to the old response is not remediation. This does not restart accepted
work in other domains. Code defects follow the incremental correction rules.
If the corrected compliance attempt still fails,
report overall `Task status: FAILED` and the failure code. No indefinite retries,
implementation dependent on rejected advice, or success after a missing skill.

Prompt instructions and self-reported evidence cannot mathematically prove model
compliance. Preserve host tool traces for review when available; never present
this protocol or the static repository validator as executable runtime enforcement.
