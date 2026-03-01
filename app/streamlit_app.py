import streamlit as st
import streamlit.components.v2 as components
import time
import requests

BACKEND_BASE_URL = "http://localhost:7860"

st.title("Assistant")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Say something"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        loading_placeholder = st.empty()
        full_response = ""

        with loading_placeholder:
            with st.spinner("Thinking..."):

                with requests.post(
                        url=f"{BACKEND_BASE_URL}/chat/stream",
                        json={"prompt": prompt},
                        stream=True,
                        timeout=60,
                ) as ai_response:
                    for chunk in ai_response.iter_content(chunk_size=None):
                        if chunk:
                            loading_placeholder.empty()
                            text = chunk.decode("utf-8")
                            full_response += text
                            message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
