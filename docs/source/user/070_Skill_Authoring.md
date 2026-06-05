# Skill Authoring Guide

How to write a skill that the agent discovers correctly, loads efficiently, and uses well.

See [Skills](069_Skills) for skill management and limits.

## SKILL.md Structure

Every skill starts with a `SKILL.md`. The only strictly required part is the YAML frontmatter at the top - everything else is recommended structure that helps the agent understand and use the skill effectively.

### Required: Frontmatter

The `---` block must appear at the very top. Both fields are required:

`````markdown
---
name: my-skill-name
description: One-line description used for discovery and triggering
---
`````

| Field | Rules |
|-------|-------|
| `name` | Lowercase letters, numbers, and hyphens only; 1-64 characters; e.g. `splunk-query-helper` |
| `description` | Written for the agent to read during discovery; be specific about when this skill applies |

**Write the description for triggering.** The agent reads only the name and description before deciding whether to activate a skill. Be specific about what situations warrant this skill. Vague descriptions cause missed activations or false positives.

Good: `"Helps write and optimize Splunk SPL queries. Use when asked to search Splunk, write a SPL query, or debug a search returning unexpected results."`

Too vague: `"Helps with log analysis."`

### Recommended Structure

A well-structured `SKILL.md` begins with an H1 title and includes at least 3 of these sections (the validator checks for them and will ask you to add more if fewer than 3 are present):

`````markdown
# My Skill Name

## When to Use
...

## Capabilities
...

## Workflow
...

## Patterns
```bash
# Include at least one code example
example here
```

## Troubleshooting
...
`````

Including at least one code example is also encouraged - the validator will prompt you to add one if none are present.

## Single-file vs Multifile Skills

**Single-file:** Everything in `SKILL.md`. Right for focused, self-contained skills - aim to keep it under ~500 lines.

**Multifile:** `SKILL.md` is a lean table of contents. The detail lives in resource files that the agent fetches on demand. Good for large reference docs, template libraries, or anything that would bloat the main document.

Conventional folder layout for multifile skills:

```
SKILL.md          # Lean index - when/how to use + list of resources
references/       # Reference docs, specs, API descriptions (conventional)
templates/        # Reusable output templates (conventional)
examples/         # Example inputs and outputs (conventional)
scripts/          # Executable Python scripts (enforced - agent can run these)
```

The `scripts/` folder is the only one with special behavior - the agent can discover and run `.py` files placed there. The other folders are naming conventions only; you can organize files however you like.

In multifile mode, the validator relaxes its section requirements (only 1 required instead of 3, no code block required) because the detail lives elsewhere.

The agent sees a listing of available resource files at the bottom of the activated skill block. It requests specific files using the `read_skill_resource` tool, so only what it actually needs lands in context.

## Writing for Context Budget

There is a limit to how much skill content the agent can hold in context at once. When that limit is reached, the least-recently-used skills are trimmed - first their resource listings, then the skills themselves. The agent is told what was cut so it can request specific sections on demand.

**What this means for authoring:**
- Keep `SKILL.md` under ~500 lines to stay comfortably within the per-skill limit
- Move large command references, example outputs, and lengthy specs into resource files
- Prefer concise, scannable sections over exhaustive prose
- Use tables and bullet lists rather than paragraphs where possible

## Python Scripts

Skills can include executable Python scripts in a `scripts/` subfolder. The agent can run these via the `run_skill_script` tool.

Declare dependencies inline using PEP 723 metadata (preferred):

```python
# /// script
# dependencies = ["requests>=2.28", "pandas"]
# ///

def main():
    import requests
    # ...

main()
```

Or list them in `scripts/requirements.txt`, one package per line.

Two extra functions are available to scripts at runtime:

- `save_artifact(name, content, content_type)` - attach a file or output to the cell
- `emit_event(event_type, data)` - send an event to the frontend

Scripts receive arguments via `sys.argv[1:]`.

## Practical Tips

**Name your skill for its trigger, not its topic.** `fix-kubernetes-oom` is better than `kubernetes` - the agent knows exactly when to reach for it.

**One skill, one job.** Skills with broad scope activate when they shouldn't and miss when they should. A focused skill with a crisp description outperforms a catch-all every time.

**Put the "when to use" section first.** The agent reads top-to-bottom; put activation criteria early so it confirms this is the right skill before reading the rest.

**Test your description.** Ask yourself: if an agent saw only the name and description, would it activate this skill at the right moment? Would it skip it at the wrong moment?

**Version your content, not your skill names.** Rename or update a skill's files rather than creating `my-skill-v2`. The skill's name is its identity in the catalog.

## Example: Minimal Valid SKILL.md

`````markdown
---
name: splunk-query-helper
description: Helps write and optimize Splunk SPL queries. Use when asked to search
  Splunk, write a SPL query, or debug a search returning unexpected results.
---

# Splunk Query Helper

## When to Use
- User asks to search Splunk for events
- User has a slow or incorrect SPL query to debug
- User wants to understand Splunk search syntax

## Capabilities
- Generate SPL queries from natural language descriptions
- Identify common performance antipatterns (missing index filter, wildcard prefix)
- Translate between SPL and other query languages

## Workflow
1. Identify the target index and time range from user context
2. Draft the SPL query
3. Check for performance issues (index filter first, field extraction order)
4. Return the query with a brief explanation

## Patterns
```spl
# Always filter by index first for performance
index=main source=/var/log/app.log level=ERROR earliest=-24h@h
| stats count by host
| sort -count
```

## Troubleshooting
- **No results:** Check index name and time range; confirm field names with `| fieldsummary`
- **Slow search:** Add `index=` filter; avoid leading wildcards in field values
`````
