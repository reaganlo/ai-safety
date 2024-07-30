# MODEL SAFETY
Evaluate safety of local LLMs.

## Build
- Install Ollama from https://ollama.com/download
- Clone the repo and `cd` into this directory.
- Run `setup.bat`

## Run

- eval_model.py
```
python src\eval_model.py
```
This program reads unsafe prompts from the `data` directory and asks the llm to classify if they are safe or unsafe. The output is generated in the `output` directory. Use the `-h (--help)` flag for usage details.