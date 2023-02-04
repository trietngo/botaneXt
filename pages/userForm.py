import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config (
    layout="wide"
)

def submission_form():
    columns = st.columns((1, 1, 1))
    with columns[1]:
        st.title("_Order A Soil Sample_")
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