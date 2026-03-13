import streamlit as st
import requests


def home_page(api):
    print("api: ", api)
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

                    with api.stream_chat(prompt) as ai_response:
                        for chunk in ai_response.iter_content(chunk_size=None):
                            if chunk:
                                loading_placeholder.empty()
                                text = chunk.decode("utf-8")
                                full_response += text
                                message_placeholder.markdown(full_response + "▌")
                        message_placeholder.markdown(full_response)

            st.session_state.messages.append({"role": "assistant", "content": full_response})
