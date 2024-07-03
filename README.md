# Guardrails for local LLMs
Proof of concept to determine the best options for implementing guardrails for locally run LLMs.

## Design Requirements
- Does not involve fine tuning of models.
- Must be run locally and offline.
- Low latency
  - Less than 0.5 seconds
- Accuracy?
  - False positives can lead to the app's unusability and missing information.
  - False Negatives can lead to vulnerabilities.
- Low memory footprint

## Key Validators
- Profanity and toxic content
- PII
  - Should certain PII's be allowed?
    E.g. In a RAG application, extracting email ids of the authors from a whitepaper.
- Prompt Injection
- Hallucination?

## Popular guardrails packages
- [Guardrails-AI] (guardrails-ai/README.md)
- [NeMo-Guardrails] (nemo-guardrails/README.md)
