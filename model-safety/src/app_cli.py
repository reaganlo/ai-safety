
import common

# Run the pipeline with a sample question
question = "What does the Rhodes Statue look like?"
print(f"QUESTION:\n{question}")
print("\n\nGenerating response...")
response = common.get_response(question)
print(f"RESPONSE:\n{response}")