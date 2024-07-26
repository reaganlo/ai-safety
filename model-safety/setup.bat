@echo off
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
ollama pull llama3
ollama pull llama2
ollama pull mistral
ollama pull phi3