# NeMo-Guardrails
You can find more details at https://github.com/NVIDIA/NeMo-Guardrails.git

## Build and Run the guardrails app
- Install Visual Studio C++ Build Tools (https://visualstudio.microsoft.com/visual-cpp-build-tools/).
- Currently requires OPENAI_API_KEY stored in a `.env` file.
- In Windows CommandPrompt, run the following from the repo root directory:
```
cd nemo-guardrails
python -m venv venv
venv\Scripts\activate.bat
setup.bat
python src\main.py
```

## Challenges
- Currently all the validations are not done locally.