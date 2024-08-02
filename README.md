# AI Safety for local LLMs
Evaluate the options for implementing safety guardrails for locally run LLMs.

## Guardrail requirements
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

## Key Vulnerabilities
- Profanity and toxic content
- Prompt Injection
- PII
  - Should certain PII's be allowed?
    E.g. In a RAG application, extracting email ids of the authors from a whitepaper.


## Guardrail options
1. [Guardrails-AI](guardrails-ai/README.md)
2. [NeMo-Guardrails](nemo-guardrails/README.md)
3. [Safety-System-Prompts](model-safety/src/safety_prompts.py)

## Model Evaluation options
1. [Model-Safety](model-safety/README.md)
2. [PyRit](https://github.com/Azure/PyRIT/blob/main/README.md)

## Guardrail Design Recommendation
1. Use non-LLM, lightweight models from [Guardrails-AI](guardrails-ai/README.md) to validate the user input and LLM output.
2. Use system prompt engineering similar to [Safety-System-Prompts](model-safety/src/safety_prompts.py) to instruct the LLM itself to behave in a safe manner.

![AI Safety Design](https://github.com/reaganlo/guardrails-llm/blob/main/guardrails-design.png?raw=true)
