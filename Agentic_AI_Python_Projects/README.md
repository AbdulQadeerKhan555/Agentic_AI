# Agentic AI Python Projects

A collection of hands-on Python projects demonstrating AI agent development using the **OpenAI Agents SDK**. Each project showcases different aspects of building intelligent, autonomous agents.

## Overview

This repository contains practical examples of AI agents built with Python, focusing on the OpenAI Agents SDK and compatible APIs. These projects range from basic agent setups to advanced implementations with tool calling, dynamic instructions, and streaming capabilities.

## Projects

| Project | Description | Key Concepts |
|---------|-------------|--------------|
| **[hello_agent](hello_agent/)** | Basic AI agent introduction | Agent setup, API integration, synchronous execution |
| **[hello_context](hello_context/)** | Context-aware agent | Context management, conversation history, stateful interactions |
| **[tool_calling](tool_calling/)** | Tool-calling agent with custom functions | Custom tools, `@function_tool` decorator, automated tool selection |
| **[searching_tool](searching_tool/)** | Web search enabled agent | Web search integration, information retrieval, real-time data |
| **[5_dynamic_instruction](5_dynamic_instruction/)** | Dynamic instruction handling | Runtime instruction modification, adaptive behavior, flexible prompting |
| **[6_streaming](6_streaming/)** | Streaming response agent | Real-time streaming, async execution, progressive responses |

## Prerequisites

- **Python 3.8+** (Python 3.10+ recommended)
- **API Key**: Gemini API key from [Google AI Studio](https://aistudio.google.com/) or OpenAI API key
- **Package Manager**: `pip` or `uv` (recommended for faster installs)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AbdulQadeerKhan555/Agentic_AI.git
cd Agentic_AI/Agentic_AI_Python_Projects
```

### 2. Choose a Project

Navigate to any project folder:

```bash
cd hello_agent
```

### 3. Install Dependencies

Each project uses the `agents` SDK:

```bash
# Using pip
pip install agents python-dotenv

# Or using uv (faster)
uv pip install agents python-dotenv
```

### 4. Configure Environment

Create a `.env` file in the project directory:

```bash
# For Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Or for OpenAI API
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Agent

```bash
python main.py
```

## Technology Stack

- **OpenAI Agents SDK**: Core framework for building AI agents
- **Gemini API**: LLM backend (OpenAI-compatible)
- **Python-dotenv**: Environment variable management
- **AsyncIO**: Asynchronous execution (for streaming projects)

## Key Concepts Covered

### 1. Agent Architecture

Each project demonstrates the fundamental components of an AI agent:

```
┌─────────────────┐
│   User Input    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Agent Runner   │
│  (Orchestrator) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  LLM Backend    │
│  (Gemini/OpenAI)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Tools/Actions  │
│  (Optional)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Response      │
└─────────────────┘
```

### 2. Tool Calling

Agents can call custom functions to perform specific tasks:

```python
@function_tool
def multiply(a: int, b: int) -> int:
    """Performs exact multiplication."""
    return a * b

@function_tool
def sum(a: int, b: int) -> int:
    """Performs exact addition."""
    return a + b
```

### 3. Context Management

Maintaining conversation history and state:

```python
# Context-aware agent retains conversation history
# Enables multi-turn conversations with memory
```

### 4. Dynamic Instructions

Modifying agent behavior at runtime:

```python
# Instructions can be updated dynamically
# Allows adaptive responses based on context
```

### 5. Streaming

Real-time response generation:

```python
# Async streaming for progressive output
# Reduces perceived latency
```

## Project Structure

```
Agentic_AI_Python_Projects/
├── hello_agent/               # Basic agent setup
│   ├── main.py
│   ├── .env.example
│   ├── .python-version
│   ├── pyproject.toml
│   └── README.md
├── hello_context/             # Context-aware agent
│   ├── main.py
│   ├── .vscode/settings.json
│   └── ...
├── tool_calling/              # Tool-calling agent
│   ├── main.py
│   └── ...
├── searching_tool/            # Web search agent
│   ├── main.py
│   └── ...
├── 5_dynamic_instruction/     # Dynamic instructions
│   ├── main.py
│   └── ...
├── 6_streaming/               # Streaming responses
│   ├── main.py
│   └── ...
└── README.md                  # This file
```

## Learning Path

### Beginner
1. **hello_agent** - Start here to understand basic agent setup
2. **hello_context** - Learn about conversation memory

### Intermediate
3. **tool_calling** - Master custom tool creation
4. **searching_tool** - Integrate external data sources

### Advanced
5. **5_dynamic_instruction** - Build adaptive agents
6. **6_streaming** - Implement real-time responses

## Common Patterns

### Agent Initialization

```python
from agents import Agent, Runner

agent = Agent(
    name="MyAgent",
    instructions="You are a helpful assistant...",
    model="gemini-2.0-flash"
)

result = Runner.run_sync(agent, "User query here")
print(result.final_output)
```

### Tool Registration

```python
from agents import function_tool

@function_tool
def my_tool(param: str) -> str:
    """Tool description."""
    return f"Result: {param}"

agent = Agent(
    name="ToolAgent",
    tools=[my_tool]
)
```

### Environment Setup

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
```

## Best Practices

### 1. API Key Management
- Never commit `.env` files to version control
- Use `.env.example` as a template
- Rotate keys periodically

### 2. Error Handling
- Implement try-catch blocks for API calls
- Handle rate limits gracefully
- Log errors for debugging

### 3. Tool Design
- Keep tools focused and single-purpose
- Provide clear docstrings
- Validate inputs before processing

### 4. Performance
- Use async/await for I/O operations
- Implement caching for repeated queries
- Monitor token usage

### 5. Testing
- Test tools independently
- Mock API responses for unit tests
- Validate agent outputs

## Troubleshooting

### Common Issues

**API Authentication Errors**
```
Solution: Verify API key in .env file is correct and active
```

**Module Not Found**
```bash
pip install agents python-dotenv
```

**Rate Limiting**
```
Solution: Implement exponential backoff or reduce request frequency
```

**Tool Not Called**
```
Solution: Ensure tool is registered and instructions mention tool usage
```

## Resources

### Documentation
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

### Related Projects
- [AI Driven Development](../AI%20driven%20development/) - Claude Code skills and workflows
- [N8N](../N8N/) - Workflow automation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - See individual project folders for details

## Author

**Abdul Qadeer Khan**

GitHub: [@AbdulQadeerKhan555](https://github.com/AbdulQadeerKhan555)

---

**Last Updated**: March 2026
**Python Version**: 3.10+
**SDK**: OpenAI Agents SDK
