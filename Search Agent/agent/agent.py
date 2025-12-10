

# Simple in-memory cache for search results
_search_cache = {}

# Set up basic logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.StreamHandler()]
)



# agent.py: Main agent orchestration logic
# Sets up the LangChain agent, loads context, and runs web search using SerpAPI and OpenAI LLM.

import os
from dotenv import load_dotenv
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from agent.context import load_pets_context




def run_web_search(query: str) -> list:
    # Step 0: Input validation
    if not isinstance(query, str) or not query.strip():
        return ["Please enter a valid search query."]

    # Step 1: Check cache first
    if query in _search_cache:
        return _search_cache[query]
    """
    Main agent entry point.
    1. Loads API keys from environment.
    2. Loads household pets context from local data file.
    3. Builds the agent prompt with pets context and user query.
    4. Initializes the LLM (OpenAI) and SerpAPI web search tool.
    5. Creates a LangChain agent that uses the LLM and SerpAPI tool.
    6. Runs the agent with the constructed prompt and returns the answer.

    Args:
        query (str): The user's search query.
    Returns:
        list: Agent's answer as a list (for Streamlit display).
    """
    # Step 2: Load environment variables
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    serpapi_api_key = os.getenv("SERPAPI_API_KEY")

    # Step 3: Check for required API keys
    if not openai_api_key or not serpapi_api_key:
        logging.error("Missing API keys. Please set OPENAI_API_KEY and SERPAPI_API_KEY in your .env file.")
        return [
            "Missing API keys. Please set OPENAI_API_KEY and SERPAPI_API_KEY in your .env file."
        ]

    # Step 4: Load household pets context from local data file
    try:
        pets_context = load_pets_context()
    except Exception as e:
        logging.exception("Failed to load pets context.")
        return [f"Error loading pets context: {e}"]

    # Step 5: Build the agent prompt with pets context and user query
    prompt = (
        "You are a helpful agent. Here is some context about household pets:\n"
        f"{pets_context}\n\n"
        f"User query: {query}\n"
        "Use the context above and web search results to answer."
    )

    # Step 6: Initialize the LLM (OpenAI) and SerpAPI web search tool
    try:
        llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
        serp_tool = Tool(
            name="SerpAPI",
            func=SerpAPIWrapper(serpapi_api_key=serpapi_api_key).run,
            description="Searches the web using SerpAPI (Google)"
        )
        # Step 7: Create a LangChain agent that uses the LLM and SerpAPI tool
        agent = initialize_agent(
            [serp_tool], llm, agent="zero-shot-react-description", verbose=True
        )
        # Step 8: Run the agent with the constructed prompt
        result = agent.run(prompt)
        # Step 9: Cache and return the agent's answer as a list (for Streamlit display)
        _search_cache[query] = [result]
        return [result]
    except Exception as e:
        logging.exception("Error during agent execution or API call.")
        # Handle common API errors
        if "rate limit" in str(e).lower():
            return ["API rate limit reached. Please wait and try again later."]
        if "timeout" in str(e).lower():
            return ["The request timed out. Please try again later."]
        return [f"An error occurred: {e}"]

