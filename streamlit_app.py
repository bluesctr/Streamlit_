import streamlit as st
import base64
from openai import OpenAI

st.title("OpenAI GPT model")

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

api_key = st.text_input(
    "OpenAI API Key",
    type="password",
    value=st.session_state.api_key
)

st.session_state.api_key = api_key

if api_key:
    client = OpenAI(api_key=api_key)
else:
    st.stop()

