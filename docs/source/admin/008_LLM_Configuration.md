# LLM Configuration

Louie supports a growing number of generative and embedding models. That includes using multiple models simultaneously and in air-gapped environments, and control of which model is used when.

Louie supports all providers implementing the OpenAI chat protocol: follow the OpenAI instructions in that case. Additionally, it natively supports a growing number of LLMs and providers, including OpenAI, Azure OpenAI, Anthropic Claude, and Groq. 

## Key concepts

### Configuration phases

You can configure:

* **Model provider connection**: Securely connect to one or more providers
* **Model registration:** Automatically or manually register individual models from a provider with a model profile name
* **Model selection:** Use the same model everywhere, or configure preferences on which model to use with which agent or agentic task

The same system is used for both generative chat models and embedding models.

### Recommended models

We generally recommend using models at the OpenAI GPT-4 level or better. This includes coverage for the following tasks:

* Smart and fast. Ex: gpt-4o for instruction following and code generation
* Smart, fast, scalable, and cheap. Ex: gpt-4o-mini for processing large amounts of data
* Large context. Ex: gpt-4.1

### Model provider authentication

You must provide connection information for your model provider(s), including potential authentication details.

Depending on the complexity of deployment, this is done in:

* `data/custom.env`: For a single global model provider
* `data/<provider>/auth.env`: When multiple providers, but at most one of each type
* `data/<provider>/auth/profile123.env`: When providers of the same type, such as due to differing model availabilities and new model testing

When multiple authentication profiles for the same provider, set distinct `AUTH_PROFILE_NAME=...` names.


### Model registration

Louie automatically detects the models exposed by some providers, such as for OpenAI. Other providers, such as Azure OpenAI, require you to explicitly register or configure your model.

Depending on the complexity of deployment, this is done in:

* `data/custom.env`: For registering a single model, or a provider that supports automatic multi-model registration
* `data/<provider>/model.env`: When multiple providers, but at most one of each type, and registering a single model or a model provider that supports automatic multi-model registration
* `data/<provider>/model/profile123.env`: When multiple models from the same provider and that provider does not support automatic multi-model registration

When multiple model profiles for the same provider, set distinct `MODEL_PROVIDER_PROFILE_NAME=...` names.

### Model selection

You configure which models are used by default. Optionally, you can further configure which models are used for specific agents and their tasks.

Model names are specified by the profile in the registration step.


### Testing

When starting Louie, you can see which model provider connections are established and which models are registered.

You can dynamically inspect what configurations are used, as a system administrator, via `/api/docs` endpoints `/api/account` and `/api/capabilities`.

### Contact staff for planning assistance

Please contact staff for assistance with AI configuration. Discussions benefit from knowledge around:

* Model service provider, e.g., Azure OpenAI vs OpenAI vs a local serving framework
* Available models
* Hardware availa7bility
* Target workloads, e.g., number of active analysts and whether any batch/continuous processing is needed



## Model selection

After connecting to your model provider and registering its models (see below), you can specify which models are used by default and for specific tasks via your `data/custom.env`:

### Default model selection

We recommend setting the below. Generally, stick to gpt-4o+ grade models. We encourage experimentation with new models such as o-series for reasoning, and performing real testing before committing to a model.

```bash
# Required
LLM_MODEL=gpt-4o

# Optional
LLM_MODEL_FAST=gpt-4o-mini
LLM_MODEL_SMART=gpt-4o
LLM_MODEL_REASONING=gpt-4o
LLM_MODEL_LARGE_CONTEXT=gpt-4o
```

### Agent model selection

Each agent, and key tasks in agents, may be configured to use specific models:

#### System agent selection

```bash
LLM_MODEL_LOUIE=
LLM_MODEL_LOUIE_MEMORY=
LLM_MODEL_MAKE_EXAMPLE=
LLM_MODEL_MAKE_RECIPE=
LLM_MODEL_TABLEQA=
LLM_MODEL_TABLEQA_ASK=
```

#### Plugin agent selection

```bash
LLM_MODEL_CHART=
LLM_MODEL_CODE=
LLM_MODEL_CYPHER=
LLM_MODEL_DATABRICKS=
LLM_MODEL_DATABRICKS_CONTEXT=
LLM_MODEL_GRAPHISTRY=
LLM_MODEL_OPENSEARCH=
LLM_MODEL_OPENSEARCH_CONTEXT=
LLM_MODEL_PANDAS=
LLM_MODEL_SPLUNK=
LLM_MODEL_SQL=
LLM_MODEL_SQL_CONTEXT=
```

### Embedding model selection

Embedding models are registered just like generative models. You may also specify which embedding model to use in general, or for specific indexes. Louie ships with out-of-the-box serving of sentence-transformers, and most model service providers also serve embedding models.

```bash
LLM_EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

OPENSEARCH_INDEX_EMBEDDING_MAPPING='{"myindex1": "text-embedding-ada-002", "myindex2":"matryoska"}'
```

## LLM Provider connection and registration

Louie LLM connection configuration is currently via environment variables. Depending on deployment complexity, place your connection configuration in:

* `data/custom.env`: Single model provider
* `data/<provider>/auth.env`: Multiple model providers, but at most one of each type
* `data/<provider>/auth/profile123.env`: Multiple model providers of the same type, such as due to differing model availabilities and new model testing

Models from providers like OpenAI are automatically registered, but for other providers, you must manually register the models:

* `data/custom.env`: Single model to register, or a provider that supports automatic multi-model registration
* `data/<provider>/model.env`: Multiple model providers, but at most one of each type, and registering a single model or a model provider that supports automatic multi-model registration
* `data/<provider>/model/profile123.env`: Multiple models from the same provider and that provider does not support automatic multi-model registration

After configuring your model provider connection and registering your models, restart the Louie server to apply the changes:

Restart the Louie server:

```bash
cd /var/louie
./dc up -d --force-recreate louie api
```

### OpenAI

1. Get an OpenAI key
2. Provider connection

    In `data/custom.env`, `data/openai/auth.env`, or `data/openai/auth/profile123.env`:

```bash
OPENAI_API_KEY=...

# OPTIONAL
OPENAI_ORGANIZATION=...
OPENAI_PROXY=...
```

3. Model registration

    You may manually register models, but typically unnecessary, in `data/custom.env`, `data/openai/model.env`, or `data/openai/models/profile123.env`.

### Azure OpenAI

1. Create Model Deployments

    Create the desired **Model Deployments** in [Azure OpenAI Studio](https://portal.azure.com/).

2. Provider connection

    In `data/custom.env`, `data/azureopenai/auth.env`, or `data/azureopenai/auth/profile123.env`:

```bash
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_API_ENDPOINT=...
```

3. Model registration

    In `data/custom.env`, `data/azureopenai/model.env`, or `data/azureopenai/model/profile123.env`:

```bash
# Azure-configured name
AZURE_DEPLOYMENT_NAME=gpt-4-latest-10Ktpm

# You can define a shorter nickname for internal use
AZURE_MODEL_NAME=gpt-4

# When using model.env or model/<profile>.env, set a unique MODEL_PROVIDER_PROFILE_NAME when using multiple models or providers to prevent name conflicts
MODEL_PROVIDER_PROFILE_NAME=azure-openai-prod-gpt-4
```

### Anthropic

1. Get API Key

    Obtain an API key from your [Anthropic](https://www.anthropic.com/) account.

2. Provider connection

    In `data/custom.env`, `data/anthropic/auth.env`, or `data/anthropic/auth/profile123.env`:

```bash
ANTHROPIC_API_KEY=...

# OPTIONAL
ANTHROPIC_API_URL=...
```

3. Model registration

    In `data/custom.env`, `data/anthropic/model.env`, or `data/anthropic/model/profile123.env`:

```bash
# OPTIONAL
MODEL_PROVIDER_PROFILE_NAME=...
```

### Groq

1. Get API Key

    Obtain an API key from your [Groq](https://www.groq.com/) account.

2. Provider connection

    In `data/custom.env`, `data/groq/auth.env`, or `data/groq/auth/profile123.env`:

```bash
GROQ_API_KEY=...

# OPTIONAL
GROQ_API_BASE=...
GROQ_PROXY=...
```

3. Model registration

    In `data/custom.env`, `data/groq/model.env`, or `data/groq/model/profile123.env`:

```bash
GROQ_CUSTOM_MODEL_NAME_OVERRIDE='cllama3-70b-8192'
```

### Sentence Transformers

Louie comes with several popular sentence transformer embedding models preloaded. See system start or `capabilities/` API for list of available models. The default recommendation is `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.

For larger deployments with many users, consider using a dedicated model server. Ex: Contact staff about configuring Nvidia Triton and other popular OSS options.