from guardrails import Guard
from guardrails.hub import ToxicLanguage
from guardrails.hub import ProfanityFree
from guardrails.hub import DetectPII
import time

VALIDATION_TYPES = ["All", "ToxicLanguage", "ProfanityFree", "DetectPII"]


def validate(validation_type, text):
    msg, total_time = "", 0.0
    if validation_type == "All":
        for vt in VALIDATION_TYPES:
            if vt != "All":
                msg, exec_time = validate_each(vt, text)
                total_time += exec_time
                if msg != "":
                    return msg, total_time
    else:
        msg, total_time = validate_each(validation_type, text)
    return msg, total_time


def validate_each(validation_type, text):
    msg, exec_time = "", 0.0
    if validation_type == "ToxicLanguage":
        guard = Guard().use(
            ToxicLanguage,
            threshold=0.75,
            validation_method="sentence",
            on_fail="exception",
        )
    elif validation_type == "ProfanityFree":
        guard = Guard().use(ProfanityFree, on_fail="exception")
    elif validation_type == "DetectPII":
        guard = Guard().use(DetectPII, ["EMAIL_ADDRESS", "PHONE_NUMBER"], "exception")

    start_time = time.time()
    try:
        guard.validate(text)
        msg = ""
    except Exception as e:
        msg = str(e)
    end_time = time.time()
    exec_time = round(end_time - start_time, 2)

    return msg, exec_time
