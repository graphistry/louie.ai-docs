# Skills

Skills are packages of specialized knowledge that you give to your agent. Each skill is a collection of markdown files (and optionally Python scripts) that teaches the agent how to handle a particular domain, workflow, or task - without you having to explain it every time.

You manage skills through the Skills panel in the UI or via the `/api/skills` endpoints.

## At a Glance

- A skill is a folder with a `SKILL.md` entry point, plus optional resource files and Python scripts.
- Skills are organization-scoped: everyone in your org shares the same catalog.
- In every conversation the agent sees the catalog - just each skill's **name** and **description** - and uses it to decide which skills are relevant.
- Activating a skill loads its full content into the agent's context; until then it costs almost nothing.
- Keep each skill focused and concise (a good rule of thumb is ~500 lines or fewer), and split large topics across multiple skills or resource files.

## What Skills Do

When you start a conversation, the agent sees a catalog of all available skills for your organization. It reads the name and description of each skill to decide which ones are relevant, then loads the full content of those it needs.

This two-step approach keeps the agent's context lean: the catalog is lightweight, and only activated skills consume context space.

## Creating a Skill

Each skill requires a `SKILL.md` file as its entry point. You can create a skill:

- **By asking the agent (recommended)** - just describe what you want and the agent writes the skill for you. This is the typical path: the agent knows the expected structure and can draft, refine, and test the skill in conversation.
- **In the UI** - through the Skills management panel
- **Via the API** - `POST /api/skills` with a name and description, then write files via the files endpoints
- **By importing an archive** - `POST /api/skills/import` with a `.zip` or `.tar.gz` containing a `SKILL.md`

Skills have limits on file count, file size, total size, allowed file types, and how many skills an organization can hold. The UI and API enforce these and report the current values, so you don't need to track exact numbers - if you exceed a limit, the system tells you which one.

## How Skills Load into the Agent

The catalog the agent reads every conversation is lightweight - just names and descriptions. Only when a skill is activated does its full content enter the agent's context, and there is a bound on how much skill content the agent holds at once. Large skills are loaded progressively: the agent pulls in the resource files it actually needs rather than everything up front.

**Practical guidance:** Keep each skill focused and concise - aim for ~500 lines or fewer. Put large reference content in separate resource files and split broad topics across multiple focused skills; the agent can fetch what it needs on demand.

## Activating Skills

A skill only takes effect once it is activated for your conversation. Activation can happen two ways:

- **You activate it** - from the Skills panel or by asking for it directly.
- **The agent activates it** - when the catalog tells it a skill fits the task.

Once active, a skill stays available in your conversation until it is deactivated. You can deactivate a skill the same ways you activate one, and the agent can drop a skill it no longer needs.

## Using Multiple Skills

Organizations can hold many skills. The agent reads all their descriptions in every conversation, so write descriptions that clearly distinguish when each skill applies. Skills with vague or overlapping descriptions lead to the agent activating the wrong one.

## Importing and Exporting

You can package a skill as a `.zip` or `.tar.gz` archive for sharing or backup. The archive must contain a `SKILL.md` at the root or top-level folder. All other files in the archive are imported as resource files.

See [Skill Authoring](070_Skill_Authoring) for how to write effective skill content.
