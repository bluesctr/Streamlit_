import streamlit as st
from openai import OpenAI

st.title("Chat Page")

api_key = st.session_state.api_key

if not api_key:
    st.write("먼저 API키를 입력하세요.")
    st.stop()

# 대화 기록 저장용 session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear 버튼
if st.button("Clear"):
    st.session_state.messages = []
    st.rerun()

@st.cache_data
def get_llm_response(messages, api_key):

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=messages
    )

    return response.output_text

# 기존 대화 출력
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력
prompt = st.chat_input("메시지를 입력하세요")

if prompt:

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.write(prompt)

    # GPT 응답 생성
    reply = get_llm_response(
        st.session_state.messages,
        api_key
    )

    # GPT 응답 저장
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    # GPT 응답 출력
    with st.chat_message("assistant"):
        st.write(reply)