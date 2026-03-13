import streamlit as st
import requests
from app.service.api_service import APIService


def login_page(api: APIService):
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = api.login(email, password)

        if response.status_code == 200:
            data = response.json()
            st.session_state.token = data["access_token"]
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

    if st.button("Go to Sign Up"):
        st.session_state.page = "signup"
        st.rerun()
