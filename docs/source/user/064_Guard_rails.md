# Guard Rails

Guard rails let an administrator add standing instructions to Louie's AI tools.
The text is injected into the tool's prompt, so it applies to every run, for
everyone in the deployment.

They are used for things that should hold regardless of what a user asks:

- House conventions — always qualify table names, prefer a particular index
- Safety limits — never run an unbounded query, always add a time range
- Output shape — answer in a fixed format, cite the source of each figure

Guard rails are not access control. They steer the model; they do not enforce.
A guard rail telling a tool not to touch a dataset is a strong hint, not a
permission boundary — use connector permissions for that.

See [Guard Rail Prompts](065_Administrators_can_set_guard_rail_prompts_on_all_or_specific_AI_tools.md)
for every variable and how to set one.
