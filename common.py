from guardrails import Guard
from guardrails.hub import ToxicLanguage
from guardrails.hub import ProfanityFree
from guardrails.hub import DetectPII
import time


def validate(guard_type, text):
    msg, exec_time = "", 0.0
    if guard_type == "ToxicLanguage":
        guard = Guard().use(
            ToxicLanguage, threshold=0.75, validation_method="full", on_fail="exception"
        )
    elif guard_type == "ProfanityFree":
        guard = Guard().use(ProfanityFree, on_fail="exception")
    elif guard_type == "DetectPII":
        guard = Guard().use(DetectPII, ["EMAIL_ADDRESS", "PHONE_NUMBER"], "exception")
    elif guard_type == "All":
        guard = Guard().use(
            ToxicLanguage(
                threshold=0.75, validation_method="full", on_fail="exception"
            ),
            ProfanityFree(on_fail="exception"),
            DetectPII(["EMAIL_ADDRESS", "PHONE_NUMBER"], on_fail="exception"),
        )

    start_time = time.time()
    try:
        guard.parse(text)
        msg = ""
    except Exception as e:
        msg = str(e)
    end_time = time.time()
    exec_time = round(end_time - start_time, 2)

    return msg, exec_time
