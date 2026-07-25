---
name: plan
description: Use for multi-step work that benefits from a short, durable task plan or handoff. Do not require a plan file for routine, single-session changes.
disable-model-invocation: true
---

# Practical Planning

## When to use

Create a plan when the user asks for one, the task will span sessions, or several
dependent changes need a clear handoff. For a small, self-contained task, use the
platform plan and proceed.

## Plan file

When a file is useful, create `plans/<task>/plan.md`. It should let the next
person resume without rediscovering the important context:

```markdown
# <Task> plan

## Goal
<Outcome and acceptance criteria>

## Context
- Branch/base: <names and commit>
- Constraints: <scope, compatibility, safety>
- Decisions: <important choices and why>

## Steps
1. [ ] Inspect the current behavior and relevant docs.
2. [ ] Make the scoped change.
3. [ ] Validate it and record the result.
4. [ ] Hand off: branch, PR, checks, and follow-ups.
```

## Working agreement

- Keep the plan accurate at meaningful milestones, after a decision, discovery,
  validation, or blocker. It is a guide, not a command log.
- Work one active step at a time and record evidence that a later reader would
  otherwise have to rediscover.
- Preserve user changes and state assumptions that materially affect scope.
- If the work changes direction, update the goal and the remaining steps before
  continuing.
- Finish with a concise resumption note: current branch, completed work,
  validation, and the next action.
