# Supported LLMs

Louie works with the LLM providers below. You need at least one. Set provider keys in `/var/louie/data/custom.env`, and see [LLM Configuration](008_LLM_Configuration.md) for model selection, multiple providers, and per-provider files.

| Provider | Main settings | Setup |
|----------|---------------|-------|
| OpenAI | `OPENAI_API_KEY` | [LLM Configuration: OpenAI](008_LLM_Configuration.md#openai) |
| Azure OpenAI | `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_API_ENDPOINT`, `AZURE_DEPLOYMENT_NAME` | [LLM Configuration: Azure OpenAI](008_LLM_Configuration.md#azure-openai) |
| Anthropic (Claude) | `ANTHROPIC_API_KEY` | [LLM Configuration: Anthropic](008_LLM_Configuration.md#anthropic) |
| Google Vertex AI (Gemini) | `VERTEX_PROJECT`, `VERTEX_LOCATION`, service account JSON | [LLM Configuration: Vertex AI](008_LLM_Configuration.md#vertex-ai) |
| AWS Bedrock | `AWS_BEARER_TOKEN_BEDROCK`, `AWS_BEDROCK_REGION` | The AWS Bedrock section of `/var/louie/system.env` |
| Groq | `GROQ_API_KEY` | [LLM Configuration: Groq](008_LLM_Configuration.md#groq) |
| Fireworks AI | `FIREWORKS_API_KEY` | The Fireworks section of `/var/louie/system.env` |
| Self-hosted or other OpenAI-compatible endpoint | `EXTERNAL_MODEL_API_BASE`, `EXTERNAL_MODEL_NAME`, `EXTERNAL_MODEL_API_KEY` | The External Model section of `/var/louie/system.env` |

`/var/louie/system.env` documents every provider setting, including proxies, token limits, and reasoning options. Copy the settings you need into `custom.env` rather than editing `system.env`.

## Choosing models

Use your provider's most capable current models for Louie's main agents. You can assign smaller, cheaper models to lighter tasks. See [Recommended models](008_LLM_Configuration.md#recommended-models) and [Model selection](008_LLM_Configuration.md#model-selection). The models you can use depend on your provider account and region.

For help choosing models, or sizing a self-hosted model, contact Graphistry.

## Self-hosted and air-gapped models

Air-gapped deployments can point Louie at a model served inside your network through an OpenAI-compatible API, such as vLLM or another inference server. Set `EXTERNAL_MODEL_API_BASE` to that server's `/v1` URL. LLM calls then stay inside your network.

## Embeddings

Some features use text embeddings. By default Louie uses your cloud provider's embedding models. To compute embeddings locally instead, see [Sentence Transformers](008_LLM_Configuration.md#sentence-transformers).
