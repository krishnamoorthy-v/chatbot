import streamlit as st
from service.api_service import APIService
from pages.home_page import home_page
from pages.login_page import login_page

BACKEND_BASE_URL = "http://localhost:7860"

api = APIService(
    base_url=BACKEND_BASE_URL,
    token=st.session_state.get("token")
)

# initialize page
if "token" not in st.session_state:
    st.session_state.page = "login"

# router
if st.session_state.page == "login":
    login_page(api)

elif st.session_state.page == "home":
    home_page(api)