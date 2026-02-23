# Hello Context Agent

An advanced AI agent demonstrating context passing and asynchronous operations with user-specific information.

## Overview

This project showcases advanced agent features including context passing, custom instructions based on user data, and asynchronous execution. The agent can access user context information and provide personalized responses.

## Features

- User context passing with `RunContextWrapper`
- Dynamic instructions using async functions
- Asynchronous agent execution
- Custom data structures with `@dataclass`
- Context-aware tool calling
- Personalized agent responses based on user information

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

The agent will process a search request with user context.

## How It Works

1. Defines a `UserContext` dataclass to store user information (username, email)
2. Creates a custom `search` tool that receives context via `RunContextWrapper`
3. Implements `special_prompt` function that generates personalized instructions
4. The agent uses user context to provide tailored responses
5. Executes asynchronously using `asyncio`

## Key Components

### UserContext
```python
@dataclass
class UserContext:
    username: str
    email: str | None = None
```

### Context-Aware Tool
The `search` tool receives `RunContextWrapper[UserContext]` to access user information during execution.

### Dynamic Instructions
The `special_prompt` function generates personalized instructions based on the user context and agent information.

## Project Structure

```
hello_context/
├── main.py          # Main agent with context passing
├── .env             # Environment variables (not tracked)
└── README.md        # This file
```

## Example Output

```
User: UserContext(username='Abdul Qadeer Khan', email=None),
Agent: MathAgent

Output: I understand you're looking for a math tutor. However, I couldn't find specific results in your area...
```

## Use Cases

- Personalized AI assistants
- User-specific recommendations
- Context-aware chatbots
- Multi-user applications with individual preferences

## License

MIT
