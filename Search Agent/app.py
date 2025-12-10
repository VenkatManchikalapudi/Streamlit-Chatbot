
import streamlit as st
from agent.agent import run_web_search

# Custom CSS for a modern look
st.markdown("""
    <style>
    .search-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d6cdf;
        margin-bottom: 0.5em;
        text-align: center;
    }
    .search-desc {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2em;
    }
    .search-box input {
        border-radius: 8px !important;
        border: 1px solid #2d6cdf !important;
        padding: 0.75em !important;
        font-size: 1.1rem !important;
    }
    .results-panel {
        background: #f6f8fa;
        border-radius: 10px;
        padding: 1.5em;
        margin-top: 2em;
        box-shadow: 0 2px 8px rgba(44,108,223,0.08);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="search-header">🔎 Custom Web Search</div>', unsafe_allow_html=True)
st.markdown('<div class="search-desc">Search the web using AI-powered LangChain agent. Enter your query below.</div>', unsafe_allow_html=True)

query = st.text_input("Search the web...", key="search_query")

if query:
    with st.spinner("Searching the web..."):
        results = run_web_search(query)
    st.markdown('<div class="results-panel">', unsafe_allow_html=True)
    st.subheader("Search Results")
    # Robustly display each result line, handling dicts and lists
    if isinstance(results, list):
        for item in results:
            if isinstance(item, dict):
                st.json(item)
            else:
                st.write(str(item))
    elif isinstance(results, dict):
        st.json(results)
    else:
        st.write(str(results))
    st.markdown('</div>', unsafe_allow_html=True)
