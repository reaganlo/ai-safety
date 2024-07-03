import os
from nemoguardrails import RailsConfig, LLMRails
from dotenv import load_dotenv

load_dotenv()


def run_example_without_rag():
    config = RailsConfig.from_path("./config")
    rails = LLMRails(config)

    response = rails.generate(
        messages=[
            {"role": "user", "content": "How many vacation days do I have per year?"}
        ]
    )
    print("Response without RAG:")
    print(response["content"])
    print()


def run_example_with_rag():
    config = RailsConfig.from_path("./config")
    rails = LLMRails(config)

    relevant_chunks = """
    Employees are eligible for the following time off:
      * Vacation: 20 days per year, accrued monthly.
      * Sick leave: 15 days per year, accrued monthly.
      * Personal days: 5 days per year, accrued monthly.
      * Paid holidays: New Year's Day, Memorial Day, Independence Day, Thanksgiving Day, Christmas Day.
      * Bereavement leave: 3 days paid leave for immediate family members, 1 day for non-immediate family members.
    """

    response = rails.generate(
        messages=[
            {"role": "context", "content": {"relevant_chunks": relevant_chunks}},
            {"role": "user", "content": "How many vacation days do I have per year?"},
        ]
    )
    print("Response with RAG:")
    print(response["content"])


def main():
    run_example_without_rag()
    run_example_with_rag()


if __name__ == "__main__":
    main()
