# imported libraries 
from utils.st import *
import pandas as pd
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="home", page_icon="🍃",
    initial_sidebar_state="collapsed",
)

remote_css("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Poppins:wght@600&display=swap")
local_css("utils/style.css")

def Title():
    st.markdown("", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3, 100, 3])
    greetings = col2.header('On the path to become a legend botanist')
    st.markdown("", unsafe_allow_html=True)


def howItWorks():
    col1, col2, col3 = st.columns([1, 1, 1])
    col2.header('How it works')


def userPropaganda():
    location = '<p style="font-family:sans serif; color:Black; font-size: 20px;">Select your location!</p>'
    customize = '<p style="font-family:sans serif; color:Black; font-size: 20px;">Customize your needs!</p>'
    startPlant = '<p style="font-family:sans serif; color:Black; font-size: 20px;">Start planting!</p>'
    col1, col2, col3 = st.columns([1, 1, 1])
    first = col1.markdown(location, unsafe_allow_html=True)
    second = col2.markdown(customize, unsafe_allow_html=True)
    third = col3.markdown(startPlant, unsafe_allow_html=True)


def goButton():
    st.markdown("""
    <style> div.stButton > button:first-child {
    background-color: rgb(0, 255, 0);}</style>""", unsafe_allow_html=True)
    columns = st.columns((3, 1, 3))
    button_pressed = columns[1].button('Let\'s get started!')
    st.markdown("", unsafe_allow_html=True)
    if button_pressed:
        switch_page("filter")


def main():
    Title()
    howItWorks()
    userPropaganda()
    goButton()


if __name__ == '__main__':
    main()
