import streamlit as st
from openai import OpenAI
from pypdf import PdfReader

st.title("PDF ChatBot")

# API KEY
api_key = st.session_state.api_key

if not api_key:
    st.write("먼저 API키를 입력하세요.")
    st.stop()

client = OpenAI(api_key=api_key)

# 대화 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# PDF 내용 저장
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# Clear 버튼
if st.button("Clear"):
    st.session_state.messages = []
    st.rerun()

# PDF 업로드
uploaded_file = st.file_uploader(
    "PDF 업로드",
    type="pdf"
)

# PDF 읽기
if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    pdf_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pdf_text += text

    st.session_state.pdf_text = pdf_text

    st.success("PDF 업로드 완료")

# 이전 대화 출력
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력
prompt = st.chat_input("질문 입력")

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

    # PDF 기반 프롬프트
    full_prompt = f"""
    다음 PDF 내용을 참고하여 답변하세요.

    PDF 내용:
    {st.session_state.pdf_text}

    이전 대화:
    {st.session_state.messages}

    사용자 질문:
    {prompt}
    """

    # OpenAI 응답 생성
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=full_prompt
    )

    reply = response.output_text

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
    