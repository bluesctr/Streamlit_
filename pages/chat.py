import streamlit as st
import base64
from openai import OpenAI

st.title("Chat Page")

api_key=st.session_state.api_key

@st.cache_data
def get_llm_response(prompt, api_key):
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt
    )

    return response.output_text

prompt = st.text_area("User prompt")

if st.button("Ask!", disabled=(len(prompt) == 0)):
    st.write(get_llm_response(prompt, api_key))

if st.button("메인으로"):
    st.switch_page("app.py")