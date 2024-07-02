import streamlit as st
import common


def main():

    st.title("Guardrails PoC")

    option = st.selectbox(
        "Validation Type:", ("ToxicLanguage", "ProfanityFree", "DetectPII", "All")
    )

    text_area = st.text_area("Enter the text to be validated:")

    if st.button("Validate"):
        if len(text_area) > 0:
            msg, exec_time = common.validate(option, text_area)
            if msg == "":
                st.success("PASS")
                st.info(f"Execution time (sec): {exec_time}")
            else:
                st.success("FAIL")
                st.info(f"Execution time (sec): {exec_time}")
                st.info(msg)


if __name__ == "__main__":
    main()
