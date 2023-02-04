import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config (
    layout="wide"
)

def submission_form():
    st.title("_Order A Soil Sample_")
    st.text_input("Name")
    st.text_input("Address")
    st.text_input("Email")

    columns = st.columns((1, 1, 1))

    
    pressed = columns[1].button("Submit")

    cancel = columns[2].button("Cancel")

    if pressed:
        switch_page("empty")

    if cancel:
        switch_page("homePage")

    

submission_form()