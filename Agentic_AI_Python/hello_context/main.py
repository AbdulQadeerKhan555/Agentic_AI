# 📦 Import Required Libraries
import os
import asyncio  # 🔄 For asynchronous programming
from dataclasses import dataclass  # 🧾 For structured data storage
from dotenv import load_dotenv, find_dotenv  # 📂 Load environment variables from .env file

from agents import (
    Agent,                           # 🤖 Core agent class
    Runner,                          # 🏃 Runs the agent
    AsyncOpenAI,                     # 🌐 OpenAI-compatible async client
    OpenAIChatCompletionsModel,      # 🧠 Chat model interface
    function_tool,                   # 🛠️ Decorator to turn Python functions into tools
    set_default_openai_client,       # ⚙️ (Optional) Set default OpenAI client
    set_tracing_disabled,            # 🚫 Disable internal tracing/logging
    ModelSettings,                    # ⚙️ Model configuration settings (if needed )
    RunContextWrapper,                # 🧑‍💻 Wrapper for passing context to tools
)
_: bool = load_dotenv(find_dotenv())  # 🔍 Load .env file and set environment variables

gemini_api_key: str | None = os.getenv("GEMINI_API_KEY")  # 🔑 Retrieve Gemini API key from environment variables

#set tracing disable
set_tracing_disabled(disabled=True)  # 🚫 Disable internal tracing/logging for cleaner output

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,
)

@dataclass
class UserContext:
    username: str
    email: str| None = None

@function_tool
async def search(local_context: RunContextWrapper[UserContext], query: str) -> str:
    import time
    time.sleep(30)  # Simulate a delay for the search operation
    return "no results found."
async def special_prompt(speical_context: RunContextWrapper[UserContext], agent: Agent) -> str:
    # who is user
    # which agent
    print(f"\nUser: {speical_context.context}, \nAgent: {agent.name}\n")
    return f"You are a math Expert. User {speical_context.context.username} is asking you to solve a math problem. Please solve the problem and provide the answer."

math_agent: Agent = Agent(
    name="MathAgent",
    instructions = special_prompt,
    model=llm_model,
    tools=[search],
)
# [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]

async def call_agent():
        # call the agent with specific input
        user_context = UserContext(username="Abdul Qadeer Khan")

        output = await Runner.run(
            starting_agent=math_agent,
            input= "search for the best math tutor in my area",
            context=user_context
)
        print(f"\n\n Output: {output.final_output}\n\n")

asyncio.run(call_agent())

