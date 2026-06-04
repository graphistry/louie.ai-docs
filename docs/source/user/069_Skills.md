# Skills

Skills are packages of specialized knowledge that you give to your agent. Each skill is a collection of markdown files (and optionally Python scripts) that teaches the agent how to handle a particular domain, workflow, or task - without you having to explain it every time.

You manage skills through the Skills panel in the UI or via the `/api/skills` endpoints.

## What Skills Do

When you start a conversation, the agent sees a catalog of all available skills for your organization. It reads the name and description of each skill to decide which ones are relevant, then loads the full content of those it needs.

This two-step approach keeps the agent's context lean: the catalog is lightweight, and only activated skills consume context space.

## Creating a Skill

Each skill requires a `SKILL.md` file as its entry point. You can create a skill:

- **In the UI** - through the Skills management panel
- **Via the API** - `POST /api/skills` with a name and description, then write files via the files endpoints
- **By importing an archive** - `POST /api/skills/import` with a `.zip` or `.tar.gz` containing a `SKILL.md`
- **By asking the agent** - the agent can create skills for you when asked

### Skill Limits

| Limit | Value |
|-------|-------|
| Skills per organization | 100 |
| Files per skill | 20 |
| Size per file | 100 KB |
| Total size per skill | 500 KB |
| Allowed file types | `.md`, `.txt`, `.json`, `.yaml`, `.yml`, `.py`, `.xml` |

## How Skills Load into the Agent

Once a skill is activated for a conversation, its content is included in the agent's context. There are limits on how much skill content fits:

| Budget | Value |
|--------|-------|
| Total across all active skills | ~10,000 tokens (40,000 characters) |
| Per skill | ~5,000 tokens (20,000 characters) |

When active skills exceed the total budget, the least-recently-used skill content is trimmed first (resource file listings are removed but the main document stays), then entire skills are evicted if needed. The most recently activated skill is never evicted. The agent is notified when content is trimmed so it can request specific sections on demand.

**Practical guidance:** Keep your main `SKILL.md` focused and concise. Put large reference content in separate resource files - the agent can fetch those on demand when it needs them.

## Activation Scopes

When a skill is activated for a conversation, it can have one of three scopes:

| Scope | Lifetime |
|-------|---------|
| `run` | Active for one agent response only |
| `session` | Active for the entire conversation |
| `explicit` | Active until manually deactivated |

Use `session` for domain knowledge relevant to a whole work session. Use `explicit` for skills that should always be available, like company-specific standards or recurring workflows.

## Using Multiple Skills

An organization can have up to 100 skills. The agent reads all their descriptions in every conversation, so write descriptions that clearly distinguish when each skill applies. Skills with vague or overlapping descriptions lead to the agent activating the wrong one.

## Importing and Exporting

You can package a skill as a `.zip` or `.tar.gz` archive for sharing or backup. The archive must contain a `SKILL.md` at the root or top-level folder. All other files in the archive are imported as resource files.

See [Skill Authoring](070_Skill_Authoring) for how to write effective skill content.
