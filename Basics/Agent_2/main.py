#  Import Required Libraries
import os
from dotenv import load_dotenv
import requests

from agents import (
    Agent,                           #  Core agent class
    Runner,                          #  Runs the agent
    AsyncOpenAI,                     #  OpenAI-compatible async client
    OpenAIChatCompletionsModel,      #  Chat model interface
    function_tool,                   #  Decorator to turn Python functions into tools
    set_tracing_disabled,            #  Disable internal tracing/logging
)

#    Load environment variables from .env file
load_dotenv()

#    Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

#    1) Environment & Client Setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  #      Get your API key from environment
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  #     Gemini-compatible base URL (set this in .env file)

#    Initialize the AsyncOpenAI-compatible client with Gemini details
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

#    2) Model Initialization
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",        #     Fast Gemini model
    openai_client=external_client
)

#  3) Define tools (functions wrapped for tool calling)
@function_tool
def subtract(a: int, b: int) -> int:
    print(f"Calculating subtraction of {a} and {b}")
    return a - b

@function_tool
def sum(a: int, b: int) -> int:
    print(f"Calculating sum of {a} and {b}")
    return a + b

#  Add Web Search Tool

# Create a tool function for web searching.
# The @function_tool decorator makes it callable by the agent automatically.
@function_tool
def web_search(query: str) -> str:
    """
    This function will act as the "search engine" for your agent.
    - Input: a string query from the user.
    - Output: some text answer fetched from the internet.
    """

    # Just to show in console what is being searched
    print(f"Searching the web for: {query}")
    
    # ---- ACTUAL SEARCH LOGIC ----
    # We are calling DuckDuckGo’s free "Instant Answer API".
    # It works without an API key and returns JSON results.
    response = requests.get(
        "https://api.duckduckgo.com/",
        params={"q": query, "format": "json"}  # send query + specify response format
    )
    
    # ---- RESPONSE HANDLING ----
    if response.status_code == 200:   # 200 means success
        data = response.json()        # convert JSON → Python dict
        abstract = data.get("AbstractText", "")  # main text result (if available)
        
        if abstract:  # if DuckDuckGo gave us a proper answer
            return abstract
        else:         # if no direct text, give a link instead
            return "No direct answer found, but here is a related link: " + data.get("AbstractURL", "")
    else:
        # If the HTTP request failed (bad internet / API issue)
        return "Search failed. Try again."


#    4) Create agent and register tools
agent: Agent = Agent(
    name="Assistant",  #     Agent's identity
    instructions=(
        "You are a helpful assistant. "
        "Always use tools for math questions. "
        "Use the web_search tool for real-time information. "  #   New instruction
        "Explain answers clearly and briefly for beginners."
    ),
    model=model, 
    tools=[sum, subtract, web_search]  #    Register tools here
)

#    5) Run the agent with a prompt (tool calling expected)
prompt = "what is 19 + 2 - 4? and why is it important to use tools for math? " \
         "Also, search for the latest news on AI advancements."
result = Runner.run_sync(agent, prompt)

#  Print the final result from the agent
print("\n CALLING AGENT\n")
print(result.final_output)