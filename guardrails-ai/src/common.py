from guardrails import Guard
from guardrails.hub import ProfanityFree
from guardrails.hub import DetectPII
from unusual_prompt import validator
import openai

import time
import concurrent.futures
import warnings

warnings.filterwarnings("ignore")

unsual_prompt = validator.UnusualPrompt(llm_callable="ollama/tinyllama")
guard = Guard().use(unsual_prompt, on="prompt", on_fail="exception")

GUARD_TYPES = ["ProfanityFree", "DetectPII", "UnusualPrompt"]


def validate(guard_types, text):
    msg, total_time = "", 0.0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for gt in guard_types:
            futures.append(executor.submit(validate_each, gt, text))
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            msg += result[0]
            total_time += result[1]
            if msg != "":
                return msg, total_time
    return msg, total_time


def validate_each(guard_type, text):
    msg, start_time, exec_time = "", time.time(), 0.0

    try:
        if guard_type == "ProfanityFree":
            guard = Guard().use(ProfanityFree, on_fail="exception")
            guard.validate(text)
        elif guard_type == "DetectPII":
            guard = Guard().use(
                DetectPII, ["EMAIL_ADDRESS", "PHONE_NUMBER"], "exception"
            )
            guard.validate(text)
        elif guard_type == "UnusualPrompt":
            unsual_prompt = validator.UnusualPrompt(llm_callable="ollama/tinyllama")
            guard = Guard().use(unsual_prompt, on="prompt", on_fail="exception")
            guard(
                openai.chat.completions.create,
                prompt=text,
                metadata={"pass_if_invalid": False},
                temperature=0.3,
                max_tokens=100,
            )
        msg = ""
    except Exception as e:
        msg = str(e)
    end_time = time.time()
    exec_time = round(end_time - start_time, 2)

    return msg, exec_time
