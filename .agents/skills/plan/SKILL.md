---
name: plan
description: Use for multi-step work that benefits from a short, durable task plan or handoff. Do not require a plan file for routine, single-session changes.
---

# Practical Planning

## Plan location and identity

Use `plans/<task>/plan.md` unless the repository specifies another location.
Start with:

```markdown
# <Task> plan

## Goal
<Outcome, not a list of implementation steps>

## Context
- Success criteria: <observable completion conditions>
- Scope and constraints: <included, excluded, safety and compatibility rules>
- Branch/base: <head, base, starting commit>
- PRs/issues/specs: <stable references>
- Decisions: <important choices and why>

## Steps

### 1.1 <Workstream>

#### 1.1.1 <First step>
**Status:** IN_PROGRESS
**Intent:** <what this establishes>
**Evidence:** <commands, files, results, or still pending>

#### 1.1.2 <Discovered step>
**Status:** TODO
**Depends on:** <step IDs or none>
```

## Hierarchical step IDs

- Give every executable step a stable three-part dotted ID such as `1.1.1`,
  `1.1.2`, `1.2.1`, or `2.1.1`. Use one- and two-part headings only to group
  steps; never give a grouping heading a status.
- Add deeper levels such as `1.1.1.1` only when a step genuinely needs
  decomposition.
- Add discovered work beneath its parent instead of renumbering unrelated
  steps. Refer to dependencies and findings by ID.
- Keep exactly one step `IN_PROGRESS` while actionable work remains. Use none
  when the plan is complete or no step can currently proceed. Other statuses
  are `TODO`, `DONE`, `BLOCKED`, and `SKIPPED`.
- A step is `DONE` only when its stated evidence proves the intended result.

## Keeping the plan useful

Update the plan at meaningful milestones: a discovery changes later work, a
decision is made, a step completes, validation changes confidence, a blocker
appears, or ownership is handed off. Do not reload or rewrite it before every
command.

When a completed step produces information needed later, copy that fact into
the dependent step as `From <step-id>: <fact and how to re-verify>`. This keeps
the plan resumable without turning it into a command transcript.

Reload the plan after a context reset, when resuming after a gap, before a
handoff, or when current work no longer matches the recorded goal. If scope
changes materially, update the goal, constraints, and affected steps before
continuing.

## Resumption and handoff

End a working session with a compact resumption block:

```markdown
## Resumption
- Current step: <ID and status>
- Completed: <IDs and evidence>
- Branch/PR: <head, base, URL>
- Validation: <passed, failed, not run>
- Decisions/blockers: <only what affects continuation>
- Next action: <one concrete action>
```

Preserve user changes, distinguish assumptions from verified facts, and never
mark the overall goal complete while required evidence is missing.
