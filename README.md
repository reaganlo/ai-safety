# AI Safety for local LLMs
Evaluate the options for implementing safety guardrails for locally run LLMs.

## Mitigation Requirements
- Does not involve fine tuning of models.
- Must be run locally and offline.
- Low latency
  - Less than 0.8 seconds?
- Accuracy
  - False Positives can lead to the app's unusability and missing information.
  - False Negatives can lead to vulnerabilities.
  - If the ideal balance cannot be achieved, the FP-FN tradeoff can be decided based on the LLM use-case.
- Low memory footprint
  - Less that 800 MB?

## Key Validators
- Profanity and toxic content
- PII
  - Should certain PII's be allowed?
    E.g. In a RAG application, extracting email ids of the authors from a whitepaper.
- Prompt Injection

## Mitigation Options
1. [Guardrails-AI](guardrails-ai/README.md)
2. [NeMo-Guardrails](nemo-guardrails/README.md)

## Evaluation Options
1. [Model-Safety](model-safety/README.md)
2. [PyRit](https://github.com/Azure/PyRIT/blob/main/README.md)

## Design Recommendation
1. Use non-LLM, lightweight models from [Guardrails-AI](guardrails-ai/README.md) to validate the user input and LLM output.
2. Use system prompt engineering similar to [Safety-System-Prompts](guardrails-ai/safety_system_prompts.py) to instruct the LLM itself to behave in a safe manner.

![AI Safety Design](https://github.com/reaganlo/guardrails-llm/blob/main/guardrails-design.png?raw=true)
