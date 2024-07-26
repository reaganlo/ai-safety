# RAG Haystack
Local RAG implementation using Haystack package.

## Build
- Install Ollama from https://ollama.com/download
- Run the following commands:

```
git clone https://github.com/reaganlo/rag-haystack.git
cd rag-haystack
setup.bat

python src\app_cli.py
python src\app_gradio.py
streamlit run src\app_streamlit.py
```