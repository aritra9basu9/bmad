# LangChain Sequential Agent Implementation

This is a ready-to-use implementation format that runs your project agents sequentially (one after another) using the registries you created:

- `.github/agents/agent-index.yaml`
- `.github/skills/skill-index.yaml`

## Files

- `sequential_agents.py`: main orchestrator
- `requirements.txt`: python dependencies
- `runs/`: generated output folder per execution

## How it works

1. Loads agent order and metadata from `agent-index.yaml`.
2. Loads skill mapping and skill markdown from `.github/skills`.
3. Invokes each agent in sequence with:
   - user goal
   - current pipeline state
   - relevant skill content
4. Passes cumulative state to next agent.
5. Writes final outputs to:
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

## Run

```powershell
python sequential_agents.py
```

Optional environment overrides:

```powershell
$env:PIPELINE_MODEL="gpt-4o-mini"
$env:PIPELINE_GOAL="Your specific implementation objective"
python sequential_agents.py
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
