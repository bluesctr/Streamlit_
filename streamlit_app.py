import streamlit as st
import base64
from openai import OpenAI

# API KEY 저장
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

st.title("OpenAI GPT model")

if st.button("채팅 페이지로 이동"):
    st.switch_page("pages/chat.py")


if st.button("이미지 페이지로 이동"):
    st.switch_page("pages/image.py")
