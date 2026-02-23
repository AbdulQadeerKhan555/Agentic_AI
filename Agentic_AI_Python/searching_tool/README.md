# Searching Tool Agent

An AI agent with web search capabilities using the Tavily API for real-time information retrieval.

## Overview

This project demonstrates how to integrate external search APIs with an AI agent. The agent can perform web searches using Tavily and answer questions based on current information from the internet.

## Features

- Web search integration using Tavily API
- Custom search tool with `@function_tool` decorator
- Real-time information retrieval
- Configurable model settings (temperature, max tokens, tool choice)
- Automatic tool selection for knowledge-based queries

## Prerequisites

- Python 3.8+
- Gemini API key from Google AI Studio
- Tavily API key from [Tavily](https://tavily.com/)

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install agents python-dotenv tavily-python
```

3. Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## Usage

Run the agent:
```bash
python main.py
```

The agent will search for: "Who is Messi?"

## How It Works

1. Initializes Tavily client for web searches
2. Creates a custom `search` tool that queries Tavily API
3. Configures the agent with model settings (temperature, tool choice, max tokens)
4. The agent automatically decides when to use the search tool
5. Returns search results in a conversational format

## Custom Tools

### search(query: str) -> str
Performs a web search using Tavily API and returns relevant results.

## Model Settings

- **Temperature**: 0.5 (balanced creativity and accuracy)
- **Tool Choice**: auto (agent decides when to use tools)
- **Max Tokens**: 500 (concise responses)

## Project Structure

```
searching_tool/
├── main.py          # Main agent with search capability
├── .env             # Environment variables (not tracked)
└── README.md        # This file
```

## Example Output

```
🤖 CALLING AGENT

Lionel Messi is an Argentine professional footballer widely regarded as one of the greatest players of all time. He currently plays for Inter Miami CF and the Argentina national team...
```

## License

MIT
