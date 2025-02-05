import streamlit as st

from output_gen import final_response

st.title("First AI Agent")
topic = st.text_input("Enter a topic:")
if "response" not in st.session_state:
    st.session_state.response = ""
if topic:

    st.session_state.response = final_response(topic=topic)
if not topic:
    st.session_state.response = ""
if st.session_state.response:
    st.write(st.session_state.response)
