import streamlit as st
import base64
from openai import OpenAI

st.title("Chat Page")

api_key=st.session_state.api_key

if not api_key:
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear 버튼
if st.button("Clear"):
    st.session_state.messages = []
    st.rerun()

@st.cache_data
def get_llm_response(prompt, api_key):
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt
    )

    return response.output_text

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.text_area("User prompt")

if st.button("Ask!", disabled=(len(prompt) == 0)):
    reply=st.write(get_llm_response(prompt, api_key))

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )
