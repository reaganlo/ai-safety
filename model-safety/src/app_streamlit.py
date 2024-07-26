import common
import streamlit as st

# Streamlit App
st.header('RAG using Ollama and Haystack')

with st.sidebar:
    st.header("Sample Questions:")
    add_radio = st.radio(
        label="sample_questions",
        label_visibility="hidden",
        options=("What are the seven wonders?", "What does the Rhodes Statue look like?", "Tell me about the Mausoleum.")
    )

# Input textbox
user_input = st.text_area("Enter Question", height=100, value=add_radio)

# Button to get response
if st.button('Get Answer'):
    if user_input:
        with st.spinner("Processing..."):
            response = common.get_response(user_input)
            st.write("**Answer:**")
            st.write(response)
    else:
        st.write("Please enter a question.")