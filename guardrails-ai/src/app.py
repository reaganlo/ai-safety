import streamlit as st
import common
import pandas as pd


def main():
    st.set_page_config(layout="wide")
    st.header("Guardrails using guardrails-ai")
    tab1, tab2 = st.tabs(["Validation Playground", "Batch Validation"])
    with tab1:
        option = st.selectbox("Validation Type:", (common.VALIDATION_TYPES))
        user_prompt = st.text_area("Enter the text to be validated:")
        if st.button("Validate", key="validate_button"):
            with st.spinner("Validating..."):
                msg, exec_time = common.validate(option, user_prompt)
                if msg == "":
                    st.success("pass")
                    st.info(f"Execution time (sec): {exec_time}")
                else:
                    st.success("fail")
                    st.info(f"Execution time (sec): {exec_time}")
                    st.info(msg)
    with tab2:
        if st.button("Batch Validate", key="batch_validate_button"):
            prompt_file = "prompts.csv"
            df = pd.read_csv(prompt_file)
            total_prompts = df.shape[0]

            with st.spinner(
                f"Validating {total_prompts} prompts from {prompt_file}. Please wait..."
            ):
                correct_results = 0
                df["actual_result"] = ""
                for _, row in df.iterrows():
                    user_prompt = str(row[0])
                    expected_result = str(row[1])
                    msg, exec_time = common.validate("All", user_prompt)
                    if msg == "":
                        actual_result = "pass"
                    else:
                        actual_result = "fail"
                    df.at[_, "actual_result"] = actual_result
                    if actual_result == expected_result:
                        correct_results += 1
                st.write(df)
                correct_percentage = (correct_results / total_prompts) * 100
                st.info(f"Correct %: {correct_percentage}")


if __name__ == "__main__":
    main()
