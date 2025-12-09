# Streamlit Chatbot

A simple chatbot application built with Streamlit and LangChain, powered by the Gemma 2B model running on Ollama.

## Features

- Interactive web-based chat interface
- Integration with LangChain for prompt management
- Local LLM support using Ollama (Gemma 2B model)
- LangSmith integration for tracking and monitoring
- Real-time response streaming

## Prerequisites

- Python 3.8 or higher
- Ollama installed with Gemma 2B model
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VenkatManchikalapudi/Streamlit-Chatbot.git
cd "Streamlit Chatbot"
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your API keys:
```
LANGCHAIN_API_KEY=your_api_key_here
LANGCHAIN_PROJECT=your_project_name
```

## Running the Application

1. Make sure Ollama is running with the Gemma 2B model:
```bash
ollama run gemma:2b
```

2. In a new terminal, run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser to `http://localhost:8501`

## Project Structure

```
Streamlit-Chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Dependencies

- `streamlit` - Web app framework
- `langchain-community` - LangChain community integrations
- `python-dotenv` - Environment variable management

## Configuration

The application uses the following environment variables:
- `LANGCHAIN_API_KEY` - Your LangChain API key
- `LANGCHAIN_PROJECT` - Your LangChain project name
- `LANGCHAIN_TRACING_V2` - Enable LangSmith tracing (set to "true")

## Usage

1. Enter your question in the text input field
2. The chatbot will process your input and return a response
3. The response is powered by the Gemma 2B model running locally via Ollama

## Notes

- This application runs the Gemma 2B model locally, so responses may be slower than cloud-based alternatives
- Ensure Ollama is properly installed and the Gemma 2B model is downloaded before running the app
- The application requires a valid LANGCHAIN_API_KEY for LangSmith integration

## License

This project is open source and available under the MIT License.

## Author

Venkat Manchikalapudi
