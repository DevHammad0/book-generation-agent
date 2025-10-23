# Book Generation Agent

An AI-powered educational content generation agent built with **OpenAI Agents SDK** that creates high-quality learning materials following a proven 5-stage teaching methodology.

## Features

- 🤖 **OpenAI Agents SDK** - Uses the official OpenAI Agents framework with `Agent` and `Runner`
- 🧭 **Minimal CLI** - Single-file `agent.py` you can run directly
- 📝 **System Prompt Driven** - Behavior defined in `system_prompt.py`

## Quick Start

### 1. Install `uv` (Recommended)

If you don't have `uv` installed:

```bash
# Linux/Mac
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -Command "irm https://astral.sh/uv/install.ps1 | iex"
```

Or visit: https://docs.astral.sh/uv/getting-started/installation/

### 2. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip (alternative)
pip install -r requirements.txt
```

### 3. Set API Key

```bash
# Linux/Mac
export OPENAI_API_KEY="sk-..."

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-..."

# Windows (Command Prompt)
set OPENAI_API_KEY=sk-...
```

### 4. Run the Agent

```bash
# Provide the request as a CLI argument
uv run agent.py "Explain Python variables"

# Or run interactively (you'll be prompted for input)
uv run agent.py

# Using python directly (alternative)
python agent.py "Explain Python variables"
```

## Project Structure

```
book-generation-agent/
├── agent.py             # Minimal CLI entrypoint (Agent + Runner)
├── system_prompt.py     # Agent behavior specification
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project metadata
└── README.md            # This file
```

## Output

- The generated content is printed to stdout.
- To save output, redirect it to a file:

```bash
uv run agent.py "Python Data Types" > Python_Data_Types.md
```

## OpenAI Agents SDK Integration

This project uses the official OpenAI Agents SDK:

```python
from agents import Agent, Runner

# Create an agent
agent = Agent(
    name="book_generation_agent",
    instructions=SYSTEM_PROMPT
)

# Run the agent
result = Runner.run_sync(agent, prompt)
content = result.final_output
```

### Key Components

- **Agent**: Configured with instructions from `system_prompt.py`
- **Runner**: Executes the agent synchronously with `Runner.run_sync()`
- **System Prompt**: Contains the methodology specification

## System Prompt

The agent's behavior is defined in `system_prompt.py`, which includes a detailed 5-stage teaching methodology and formatting guidelines.

## Troubleshooting

### API Key Not Found

```
ERROR: OPENAI_API_KEY is not set
```

**Solution:** Set your API key:

```bash
export OPENAI_API_KEY="sk-..."   # Linux/Mac
$env:OPENAI_API_KEY="sk-..."     # Windows (PowerShell)
set OPENAI_API_KEY=sk-...         # Windows (CMD)
```

### Agents SDK Version

Make sure you have a compatible version of `openai-agents`:

```bash
# Using uv (recommended)
uv pip install --upgrade openai-agents

# Or using pip (alternative)
pip install --upgrade openai-agents
```

## Requirements

- Python 3.10 or higher
- OpenAI API key with Agent access
- `openai-agents` package

## Next Steps

1. **Install** - Run `uv sync` (or `pip install -r requirements.txt`)
2. **Configure** - Set `OPENAI_API_KEY`
3. **Run** - `uv run agent.py "Your topic"` or `uv run agent.py` (interactive)
4. **Customize** - Edit `system_prompt.py` if needed

## License

This project uses OpenAI's API. Ensure compliance with OpenAI's terms of service.

---

Ready to generate educational content?

```bash
uv run agent.py "Your topic here"
```
