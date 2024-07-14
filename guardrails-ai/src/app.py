import streamlit as st
import common
import pandas as pd


def main():
    st.set_page_config(layout="wide")
    st.header("Guardrails using guardrails-ai")
    tab1, tab2 = st.tabs(["Playground", "Batch Evaluation"])
    with tab1:
        option = st.selectbox("Select Guard Type:", (common.GUARD_TYPES))
        user_prompt = st.text_area("Enter the text to be validated:")
        if st.button("Validate"):
            with st.spinner("Validating..."):
                msg, exec_time = common.validate(option, user_prompt)
                if msg == "":
                    st.success("safe")
                    st.success(f"Execution time (sec): {exec_time}")
                else:
                    st.error("unsafe")
                    st.error(msg)
                    st.error(f"Execution time (sec): {exec_time}")
    with tab2:
        st.write(
            "Click the button to evaluate the prompts in the **prompts.csv** file."
        )
        if st.button("Batch Evaluate"):
            prompt_file = "prompts.csv"
            df = pd.read_csv(prompt_file)
            total_prompts = df.shape[0]

            with st.spinner(f"Evaluating {total_prompts} prompts. Please wait..."):
                correct_results, total_time = 0, 0.0
                df["actual_result"] = ""
                for _, row in df.iterrows():
                    user_prompt = str(row[0])
                    expected_result = str(row[1])
                    msg, exec_time = common.validate("All", user_prompt)
                    if msg == "":
                        actual_result = "safe"
                    else:
                        actual_result = "unsafe"
                    df.at[_, "actual_result"] = actual_result
                    df.at[_, "exec_time"] = exec_time
                    if actual_result.lower() == expected_result.lower():
                        correct_results += 1
                    total_time += exec_time
                st.write(df)
                correct_percentage = (correct_results / total_prompts) * 100
                avg_time = total_time / total_prompts
                st.info(f"**Accuracy (%)**: {correct_percentage}")
                st.info(f"**Avg Time (sec)**: {avg_time}")


if __name__ == "__main__":
    main()
