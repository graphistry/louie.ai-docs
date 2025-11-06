# Recipes

## Overview

Recipes are designed for multi-step workflows and complex processes that need to be repeated consistently.

## Recipe Levels

There are two levels of recipes available:

- **System-level**: Available for all users, only admin-editable
- **Organization-level**: Available for all org users, only org-admin-editable

## Working with Recipes

### Viewing Recipes
To view existing recipes, tell Louie to run:
- `ListOrgRecipesAgent` - for organization-level recipes
- `ListSystemRecipesAgent` - for system-level recipes

### Creating Recipes
To create new recipes:
1. Tell Louie to create a draft via `UserAuthorRecipeAgent`
2. Save the recipe using:
   - `SaveOrgRecipeAgent` - for organization-level recipes
   - `SaveSystemRecipeAgent` - for system-level recipes

## Recipe Use Cases

Recipes are ideal for:
- Multi-step workflows that need to be repeated
- Complex processes that require consistent execution
- Procedures that involve multiple tools or agents

![Recipes Example](./images/user/057_Recipes_1.png)

