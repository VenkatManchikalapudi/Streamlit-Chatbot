# Copilot Instructions for LangChain Web Search Agent Project

This project is a Python-based web search agent using LangChain for search logic and Streamlit for the web interface.

## Architecture Overview
- **LangChain**: Used for agent logic, web search, and result parsing.
- **Streamlit**: Provides a simple, interactive web UI for user queries and displaying results.
- **Main Components**:
  - `app.py`: Streamlit entry point, handles user input and displays results.
  - `agent/`: Contains LangChain agent setup and search logic.
  - `requirements.txt`: Lists dependencies (langchain, streamlit, plus any web search tools).

## Developer Workflows
- **Install dependencies**: `pip install -r requirements.txt`
- **Run app**: `streamlit run app.py`
- **Add new search tools**: Extend `agent/` with new LangChain tools or chains.
- **Debugging**: Use Streamlit's live reload and LangChain's verbose logging for troubleshooting.

## Project Conventions
- All agent logic lives in `agent/`.
- Streamlit UI code is only in `app.py`.
- Use environment variables for API keys (e.g., web search APIs).
- Prefer LangChain's built-in tools for web search unless custom logic is required.

## Integration Points
- External web search APIs (e.g., SerpAPI, Bing, DuckDuckGo).
- Streamlit for UI.
- LangChain for agent orchestration.

## Example Usage
- Start the app: `streamlit run app.py`
- Enter a query in the UI, agent searches the web and displays results.

## Key Files
- `app.py`: Streamlit UI and main loop.
- `agent/agent.py`: LangChain agent setup and search logic.
- `requirements.txt`: Python dependencies.

## Tips for AI Agents
- Always check `requirements.txt` for dependencies.
- Use LangChain's documentation for agent/tool patterns.
- Keep UI logic and agent logic separate.
- Reference environment variables for sensitive info.

---
Update this file as the project evolves. For more details, see https://aka.ms/vscode-instructions-docs.
