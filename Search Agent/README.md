# LangChain Streamlit Web Search Agent

This project is a Streamlit web app powered by a LangChain agent. It combines local context (household pets data) and live web search (via SerpAPI) to answer user queries using an LLM (OpenAI/ChatOpenAI).

## Features
- **Conversational agent**: Uses ChatOpenAI for natural, context-aware answers.
- **Web search integration**: Uses SerpAPI for up-to-date web results.
- **Local context**: Loads and injects structured data from `data/pets.json`.
- **Streamlit UI**: Simple, modern web interface for user queries.

## Setup
1. **Clone the repo**
2. **Create a virtual environment**
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Add your API keys**
   - Create a `.env` file with:
     ```
     OPENAI_API_KEY=your-openai-key
     SERPAPI_API_KEY=your-serpapi-key
     ```
5. **Run the app**
   ```
   streamlit run app.py
   ```

## File Structure
```
Search Agent/
├── app.py                # Streamlit UI
├── agent/
│   ├── agent.py          # Agent logic (LLM, tools, orchestration)
│   ├── context.py        # Loads pets context
│   └── __init__.py
├── data/
│   └── pets.json         # Household pets data
├── requirements.txt      # Dependencies
├── .env                  # API keys (not committed)
├── .gitignore
└── README.md
```

## Customization
- Edit `data/pets.json` to add more pets or fields as needed.
- Update `agent/context.py` to load and format new context fields.
- Swap out the web search tool or LLM as needed.

## Notes
- Make sure your API keys are valid and not rate-limited.
- For production, consider adding error handling, caching, and user authentication.

---

For more details, see `.github/copilot-instructions.md` or ask for help!
