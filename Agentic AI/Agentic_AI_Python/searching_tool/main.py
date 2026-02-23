# 📦 Import Required Libraries
import os
from dotenv import load_dotenv, find_dotenv  # 📂 Load environment variables from .env file

from agents import (
    Agent,                           # 🤖 Core agent class
    Runner,                          # 🏃 Runs the agent
    AsyncOpenAI,                     # 🌐 OpenAI-compatible async client
    OpenAIChatCompletionsModel,      # 🧠 Chat model interface
    function_tool,                   # 🛠️ Decorator to turn Python functions into tools
    set_default_openai_client,       # ⚙️ (Optional) Set default OpenAI client
    set_tracing_disabled,            # 🚫 Disable internal tracing/logging
    ModelSettings                    # ⚙️ Model configuration settings (if needed
)
from tavily import TavilyClient  # 🌐 Tavily client for Gemini (if needed for advanced features)

# 🌿 Load environment variables from .env file
load_dotenv(find_dotenv())

# 🚫 Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

# 🔐 1) Environment & Client Setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 🔑 Get your API key from environment
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")  # 🔑 (Optional) Tavily API key if using advanced features
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  # 🌐 Gemini-compatible base URL (set this in .env file)


# 🌐 Optional: Initialize Tavily client for advanced Gemini features
tavily_client: TavilyClient = TavilyClient(    
    api_key=TAVILY_API_KEY        
    )  
reponse = tavily_client.search("who is messy?")

# 🌐 Initialize the AsyncOpenAI-compatible client with Gemini details
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

# 🧠 2) Model Initialization
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",        # ⚡ Fast Gemini model
    openai_client=external_client
)

# 🛠️ 3) Define tools (functions wrapped for tool calling)
@function_tool
def search(query: str) -> str:
    """🔍 Search tool (use this for general knowledge questions)."""
    print("Tool for searching called with query:", query)
    response = tavily_client.search(query)
    return response


# 🤖 4) Create agent and register tools
agent: Agent = Agent(
    name="Search Agent",  # 🧑‍🏫 Agent's identity
    model=model,
    tools=[search],  # 🛠️ Register tools here
    model_settings=ModelSettings(           # ⚙️ Optional model settings
        temperature=0.5, 
        tool_choice="auto", 
        max_tokens=500
        )  
)

# 📝 5) Define a prompt for the agent
prompt = "Who is messy?"

# 🏃 Run the agent with the prompt
result = Runner.run_sync(agent, prompt)

# 📤 Print the final result from the agent
print("\n🤖 CALLING AGENT\n")
print(result.final_output)