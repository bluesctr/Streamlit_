import streamlit as st
from openai import OpenAI

st.title("부경대 도서관 챗봇")

api_key = st.session_state.api_key

if not api_key:
    st.write("먼저 API키를 입력하세요.")
    st.stop()
    