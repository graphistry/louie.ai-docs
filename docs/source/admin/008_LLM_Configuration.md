# Security Level Configuration

Adjust the security level for LLM interactions in the `custom.env` file:

## LLM_PRIVACY_LEVEL

  - `NO_LLM`: No LLM connected; nothing is sent to an LLM.
  - `METADATA`: Only questions and database schemas are sent to the LLM (e.g., for query generation).
  - `DATA`: LLM can see table values.

### To Disable LLM

```bash
LLM_PRIVACY_LEVEL=NO_LLM
```


## LLM Model Configuration

### OpenAI

#### 1. Configure LLM

Edit the file `/var/louie/data/custom.env`.

**Note:** No AI agents will function without registering an LLM.

Set the following configurations:

```bash
OPENAI_API_KEY=...

# Pick models for each category:
# base, high-quality, long-context, & embedding
LLM_MODEL='gpt-3.5-turbo'
LLM_MODEL_4='gpt-4'
LLM_MODEL_16='gpt-3.5-turbo-16k'
LLM_EMBEDDING_MODEL='text-embedding-ada-002'

# OPTIONAL
OPENAI_ORGANIZATION=...
OPENAI_PROXY=...
```

### 2. Restart Server

Restart the Louie server:

```bash
cd /var/louie
./dc up -d --force-recreate louie api
```

---

### Azure OpenAI

#### 0. Create Model Deployments

Create the desired **Model Deployments** in [Azure OpenAI Studio](https://portal.azure.com/).

#### 1. Configure LLM

Edit the file `/var/louie/data/custom.env`.

**Note:** No AI agents will function without registering an LLM.

Set the following configurations:

```bash
# Set authentication
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_API_ENDPOINT=...

# Configure desired model assignment for each category:
# LLM_MODEL (base), LLM_MODEL_4 (high-quality),
# LLM_MODEL_16 (long-context), & LLM_EMBEDDING_MODEL (embedding APIs)
LLM_MODEL='gpt-4'
LLM_MODEL_4='gpt-4'
LLM_MODEL_16='gpt-4'
LLM_EMBEDDING_MODEL='sentence-transformers/paraphrase-MiniLM-L6-v2'

# If registering only one model deployment
AZURE_DEPLOYMENT_NAME='gpt-4-latest-mydeploy1'
AZURE_MODEL_NAME='gpt-4'
```

To register multiple model deployments, create multiple `.env` files under `/var/louie/data/data/azureopenai/models/`, one per model. For example:

```bash
# Example .env file for a model deployment
AZURE_DEPLOYMENT_NAME='gpt-4-latest-mydeploy2'
AZURE_MODEL_NAME='gpt-4'
```

**Recommendation:** Use three models—GPT-3.5, GPT-4, and a long-context variant.

#### 2. Restart Server

Restart the Louie server:

```bash
cd /var/louie
./dc up -d --force-recreate louie api
```

**Contact staff** for Azure and Louie configuration assistance.

**Tip:** Check the Louie container start logs at DEBUG level to see why configurations are or are not loading.

**Note:** GPT-4 is currently available only in limited regions (e.g., **US East 1** and **US East 2**). Refer to [GPT-4 and GPT-4 Turbo Model Availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-preview-model-availability) for more details.

---

### Anthropic

#### 0. Get API Key

Obtain an API key from your [Anthropic](https://www.anthropic.com/) account.

#### 1. Configure LLM

Edit the file `/var/louie/data/custom.env`.

**Note:** No AI agents will function without registering an LLM.

Set the following configurations:

```bash
# Set authentication
ANTHROPIC_API_KEY=...

# Configure desired model assignment for each category:
# LLM_MODEL (base), LLM_MODEL_4 (high-quality),
# LLM_MODEL_16 (long-context), & LLM_EMBEDDING_MODEL (embedding APIs)
LLM_MODEL='claude-3-opus-20240229'
LLM_MODEL_4='claude-3-opus-20240229'
LLM_MODEL_16='claude-3-opus-20240229'
LLM_EMBEDDING_MODEL='sentence-transformers/paraphrase-MiniLM-L6-v2'
```

#### 2. Restart Server

Restart the Louie server:

```bash
cd /var/louie
./dc up -d --force-recreate louie api
```

**Contact staff** for configuration assistance.

**Tip:** Check the Louie container start logs at DEBUG level to see why configurations are or are not loading.

---

### Groq

#### 0. Get API Key

Obtain an API key from your [Groq](https://www.groq.com/) account.

#### 1. Configure LLM

Edit the file `/var/louie/data/custom.env`.

**Note:** No AI agents will function without registering an LLM.

Set the following configurations:

```bash
# Set authentication
GROQ_API_KEY=...

# Load your model
GROQ_CUSTOM_MODEL_NAME_OVERRIDE='cllama3-70b-8192'

# Configure desired model assignment for each category:
# LLM_MODEL (base), LLM_MODEL_4 (high-quality),
# LLM_MODEL_16 (long-context), & LLM_EMBEDDING_MODEL (embedding APIs)
LLM_MODEL='cllama3-70b-8192'
LLM_MODEL_4='cllama3-70b-8192'
LLM_MODEL_16='cllama3-70b-8192'
LLM_EMBEDDING_MODEL='sentence-transformers/paraphrase-MiniLM-L6-v2'
```

#### 2. Restart Server

Restart the Louie server:

```bash
cd /var/louie
./dc up -d --force-recreate louie api
```

**Contact staff** for configuration assistance.

**Tip:** Check the Louie container start logs at DEBUG level to see why configurations are or are not loading.

**Note:** Groq relies on open-source models, which may require additional configuration and usage training for satisfactory results.

---

Feel free to reach out if you need further assistance with the configurations.


TODO(tcook):  add details on sentence transformers?  Does each LLM have it's own config options that need to be added here? 

