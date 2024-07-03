@echo off
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
guardrails hub install hub://guardrails/toxic_language
guardrails hub install hub://guardrails/profanity_free
guardrails hub install hub://guardrails/detect_pii
