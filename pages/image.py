import streamlit as st
import base64
from openai import OpenAI

st.title("Image Page")

@st.cache_data
def generate_image(image_prompt, api_key):
    client = OpenAI(api_key=api_key)

    img = client.images.generate(
        model="gpt-image-1-mini",
        prompt=image_prompt
    )

    image_bytes = base64.b64decode(img.data[0].b64_json)

    return image_bytes

image_prompt = st.text_area("Image prompt")

if st.button("Generate!", disabled=(len(image_prompt) == 0)):
    st.image(generate_image(image_prompt, api_key))

if st.button("메인으로"):
    st.switch_page("app.py")