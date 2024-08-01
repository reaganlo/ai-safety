import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Model Safety Dashboard")

# File uploader
uploaded_file = st.file_uploader("Choose model evaluation CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Check if 'actual_result' column exists
    if "actual_result" in df.columns:
        # Group by 'actual_result' and count occurrences
        result_counts = df["actual_result"].value_counts()

        # Generate pie chart
        fig, ax = plt.subplots()
        ax.pie(
            result_counts, labels=result_counts.index, autopct="%1.1f%%", startangle=90
        )
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display pie chart
        st.pyplot(fig)
    else:
        st.error("The CSV file does not contain an 'actual_result' column.")
