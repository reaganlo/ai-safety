@echo off

python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
guardrails hub install hub://guardrails/profanity_free
guardrails hub install hub://guardrails/detect_pii
