# Guardrails-AI
You can find more details at https://github.com/guardrails-ai/guardrails.git

## Build and Run the guardrails app
- In Windows CommandPrompt, run the following from the repo root directory:
```
cd guardrails-ai
python -m venv venv
venv\Scripts\activate.bat
setup.bat
streamlit run src\app.py
python src\test_prompt_injection.py
```

## Key Validators
- **profanity_free** (https://github.com/guardrails-ai/profanity_free.git)

    Based on `alt-profanity-check` python package.
    Uses a linear SVM trained on 200K user labeled data from twitter and wikipedia. Uses the concept of Bag of Words to determine the words that are generally related to toxic content. Size is ~1MB. We can use it as part of the input and output guards.

- **detect_pii** (https://github.com/guardrails-ai/detect_pii)

    Based on Microsoft's Presidio package. Uses the SpaCy NLP model `en_core_web_lg`. Size is around ~600MB. We could use it as part of the output guard to filter out PIIs.

- **unsual_prompt** (https://github.com/reaganlo/unusual_prompt.git)

    Can be used as a safety system prompt wrapper around the main LLM calls.
