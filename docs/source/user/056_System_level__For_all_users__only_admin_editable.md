# System-level: For All Users, Only Admin-editable

## Overview

There are two levels of examples and recipes in Louie:

- **System-level**: Available for all users, only admin-editable
- **Organization-level**: Available for all org users, only org-admin-editable

## Working with Examples

### Viewing Examples
To view existing examples, tell Louie to run:
- `ListOrgExamplesAgent` - for organization-level examples
- `ListSystemExamplesAgent` - for system-level examples

### Creating Examples
To create new examples:
1. Tell Louie to create a draft via `MakeExamplesAgent` or `UserAuthorExamplesAgent`
2. Save the examples using `SaveOrgExamplesAgent` or `SaveSystemExamplesAgent`

## Examples Use Cases

Examples are ideal for simple scenarios and facts that can be quickly referenced and applied.

![System Level Examples](./images/user/056_System_level__For_all_users__only_admin_editable_1.png)

