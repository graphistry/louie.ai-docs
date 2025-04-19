# LLM Authorization 

Adjust the security level for LLM interactions controlling what kind of data is sent to the LLM during database interactions:

  - `NO_LLM`: No LLM connected; nothing is sent to an LLM.
  - `METADATA`: Only questions and database schemas are sent to the LLM (e.g., for query generation).
  - `DATA`: LLM can see table values.

Configure each setting by specifying `LLM_PRIVACY_LEVEL=...` in `custom.env`.

### To Disable LLM

```bash
LLM_PRIVACY_LEVEL=NO_LLM
```


Authorization: LLM Comply with oversharing and AI-decision-making policies
Data flow OpenAI or any LangChain-compatible (Azure OpenAI, AWS Bedrock, Llama2, Falcon, Mistral, …)
can be connected; typically configured to NOT learn from user queries to avoid data leakage

Set LLM_PRIVACY_LEVEL=...
NO_LLM: No LLM connected; nothing sent to LLM; no AI decision making METADATA: User query, database schema, and previous outputs go to LLM… but no table values . Minor leakage to LLM such as analyst intent, special values in queries, etc. AI generates queries and code, but analyst checks, and does all data interpretation. DATA: Data table contents sent to LLM for analysis, e.g., Table AI agent
 Louie learns from usage too
Louie builds a database of context to learn smarter queries over time (RAG) Currently: Query history limited to same-dthread Upcoming: Control widening scope to organizational sharing unit (RBAC), e.g., personal account vs team




