import os
import argparse
import pandas as pd
import safety
import warnings
import logger
from logger import logging

warnings.filterwarnings("ignore")


def main(args):
    df = pd.read_csv(args.prompt_file)
    total_prompts = df.shape[0]
    print(f"Evaluating model safety with {total_prompts} prompts. Please wait..")

    correct_results, total_time = 0, 0.0
    df["actual_result"] = ""
    for idx, row in df.iterrows():
        user_prompt = str(row[0])
        expected_result = str(row[1])
        actual_result, exec_time = safety.check_safety(args.model, user_prompt, 0)
        df.at[idx, "actual_result"] = actual_result
        df.at[idx, "exec_time"] = exec_time
        if actual_result.lower() == expected_result.lower():
            correct_results += 1
        total_time += exec_time

    correct_percentage = (correct_results / total_prompts) * 100
    avg_time = total_time / total_prompts
    print(f"Accuracy (%): {correct_percentage}")
    print(f"Avg response time (sec): {avg_time}")

    output_file = f"{args.model}_{logger.RUN_TS}.csv"
    output_path = os.path.join(os.getcwd(), "output")
    os.makedirs(output_path, exist_ok=True)
    OUTPUT_FILE_PATH = os.path.join(output_path, output_file)

    df.to_csv(OUTPUT_FILE_PATH, index=False)
    print(f"Results saved to {OUTPUT_FILE_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Argument parser")
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="phi3",
        help="Model name (e.g., phi3)",
    )
    parser.add_argument(
        "-p",
        "--prompt_file",
        type=str,
        default="data\harmbench_behaviors_text_small.csv",
        help="CSV file containing prompts",
    )

    parser.add_argument(
        "-l",
        "--log_level",
        type=str,
        default="info",
        help="Log levels: debug, info, warning, error, critical",
    )

    args = parser.parse_args()
    logger.set_logger(prefix=args.model, log_level=args.log_level)

    msg = f"Model: {args.model}"
    logging.info(msg)
    print(msg)

    msg = f"Prompt file: {args.prompt_file}"
    logging.info(msg)
    print(msg)

    msg = f"Log level: {args.log_level}"
    logging.info(msg)
    print(msg)

    main(args)
