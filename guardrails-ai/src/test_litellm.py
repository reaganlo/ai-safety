from litellm import completion


def chatbot(prompt):
    response = completion(
        model="ollama/phi3",
        messages=[{"role": "user", "content": prompt}],
        api_base="http://localhost:11434",
    )
    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    while True:
        user_input = input("USER: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        print("BOT: " + chatbot(user_input))
        print("\n")
