import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config (
    page_title="User form", page_icon="",
    initial_sidebar_state="collapsed",
    layout="wide"
)
m = st.markdown("""
    <style>
    body{
        background-color: #5b7357
    }
    div.stButton > button {
        background-color: #e3e8c5;
        color:#2b3115;
        border: none;
        padding: 15px 32px;
    }
    div.stButton > button:hover {
        background-color: #5b7357;
        color:#fdfdfd;
        border: none;
    }
    t1 {
        font-size: 20px;
        color:#2b3115;
    }
    </style>""", unsafe_allow_html=True)

def submission_form():
    columns = st.columns((1, 1, 1))
    with columns[1]:
        st.title("_Order a Soil Sample_")
        st.text_input("Name")
        st.text_input("Address")
        st.text_input("Email")

    pressed = columns[1].button("Submit")

    cancel = columns[1].button("Cancel")

    if pressed:
        switch_page("thank_you")

    if cancel:
        switch_page("homePage")



submission_form()