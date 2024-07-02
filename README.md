# Guardrails for local LLMs
Proof of concept to determine the best options for implementing guardrails for locally run LLMs.

## Design Requirements
- Does not involve fine tuning of models.
- Must be run locally and offline.
- Low latency
- Accuracy?
  - False positives can lead to the app's unusability and missing information.
  - False Negatives can lead to vulnerabilities.

## Key Validators
- Profanity and toxic content
- PII
  - Should certain PII's be allowed?
    E.g. In a RAG application, extracting email ids of the authors from a whitepaper.
- Prompt Injection
- Hallucination?

## Popular guardrails packages
- Guardrails AI (https://github.com/guardrails-ai/guardrails.git)
- NeMo-Guardrails by Nvidia (https://github.com/NVIDIA/NeMo-Guardrails.git)

The current package of choice is **Guardrails AI**.

## Build demo

```
python -m venv venv
venv\Scripts\activate.bat
setup.bat
```
## Run demo

```
streamlit run app.py
```

## Challenges
- Currently there are no options to detect Prompt Injection locally.
