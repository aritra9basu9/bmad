# LangChain Sequential Agent Implementation

This is a ready-to-use implementation format that runs your project agents sequentially (one after another) using the registries you created:

- `.github/agents/agent-index.yaml`
- `.github/skills/skill-index.yaml`

## Files

- `sequential_agents.py`: main orchestrator
- `rag_redis.py`: Redis-backed RAG indexing and retriever
- `integrations.py`: JIRA/Confluence/Xray API integration helpers
- `requirements.txt`: python dependencies
- `runs/`: generated output folder per execution

## How it works

1. Loads agent order and metadata from `agent-index.yaml`.
2. Loads skill mapping and skill markdown from `.github/skills`.
3. Optionally loads Redis RAG context from planning and implementation artifacts.
4. Invokes each agent in sequence with:
   - user goal
   - current pipeline state
   - retrieved RAG context
   - relevant skill content
5. Passes cumulative state to next agent.
6. Optionally publishes results to JIRA/Confluence/Xray.
7. Writes final outputs to:
   - `langchain-implementation/runs/run-<timestamp>/result.json`
   - `langchain-implementation/runs/run-<timestamp>/result.md`

## Setup

```powershell
cd langchain-implementation
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Set your API key:

```powershell
$env:OPENAI_API_KEY="your_key_here"
```

Set Redis for vector store:

```powershell
$env:REDIS_URL="redis://localhost:6379"
$env:REDIS_INDEX_NAME="bmad-project-index"
```

Optional: force re-index before run:

```powershell
$env:RAG_REINDEX="true"
```

## Run

```powershell
python sequential_agents.py
```

Optional environment overrides:

```powershell
$env:PIPELINE_MODEL="gpt-4o-mini"
$env:PIPELINE_GOAL="Your specific implementation objective"
$env:PIPELINE_USE_RAG="true"
$env:PIPELINE_PUBLISH_MGMT="false"
python sequential_agents.py
```

## JIRA / Confluence / Xray integration (optional)

Set env vars and enable publishing:

```powershell
$env:PIPELINE_PUBLISH_MGMT="true"

$env:JIRA_BASE_URL="https://your-domain.atlassian.net"
$env:JIRA_EMAIL="you@company.com"
$env:JIRA_API_TOKEN="jira_token"
$env:JIRA_PROJECT_KEY="ATP"

$env:CONFLUENCE_BASE_URL="https://your-domain.atlassian.net"
$env:CONFLUENCE_EMAIL="you@company.com"
$env:CONFLUENCE_API_TOKEN="confluence_token"
$env:CONFLUENCE_SPACE_KEY="ENG"

$env:XRAY_BASE_URL="https://xray.cloud.getxray.app"
$env:XRAY_CLIENT_ID="xray_client_id"
$env:XRAY_CLIENT_SECRET="xray_client_secret"
```

## Agent order

Order is exactly as defined in `.github/agents/agent-index.yaml`:
1. analyst
2. pm
3. architect
4. developer
5. tech-writer
6. ux-designer

If you want a different execution order, edit `agent-index.yaml`.
