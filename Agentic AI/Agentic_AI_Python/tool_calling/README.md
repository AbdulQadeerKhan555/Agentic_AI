# Tool Calling Agent

An AI agent that demonstrates tool calling capabilities using custom Python functions for mathematical operations.

## Overview

This project showcases how to create custom tools (functions) that an AI agent can call to perform specific tasks. The agent uses the Gemini API and can perform exact mathematical calculations using defined tools.

## Features

- Custom tool creation using `@function_tool` decorator
- Math operations (multiplication and addition)
- Automatic tool selection by the agent
- DMAS rule following (Division, Multiplication, Addition, Subtraction)
- Clean output with disabled tracing

## Prerequisites

- Python 3.8+
- Gemini API key from Google AI Studio

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install agents python-dotenv
```

3. Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

Run the agent:
```bash
python main.py
```

The agent will solve: "What is 19 + 23 * 2?"

## How It Works

1. Defines custom tools (`multiply` and `sum`) using the `@function_tool` decorator
2. Creates an agent with instructions to use tools for math operations
3. Registers the tools with the agent
4. The agent automatically decides which tools to call based on the query
5. Returns the final calculated result

## Custom Tools

### multiply(a: int, b: int) -> int
Performs exact multiplication of two integers.

### sum(a: int, b: int) -> int
Performs exact addition of two integers.

## Project Structure

```
tool_calling/
├── main.py          # Main agent with tool calling
├── .env             # Environment variables (not tracked)
└── README.md        # This file
```

## Example Output

```
🤖 CALLING AGENT

First, I'll multiply 23 by 2, then add 19 to the result.
23 * 2 = 46
19 + 46 = 65

The answer is 65.
```

## License

MIT
