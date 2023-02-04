# imported libraries
from utils.st import *
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import base64
import streamlit as st

st.set_page_config(
    page_title="home", page_icon="🍃",
    initial_sidebar_state="collapsed",
)
def add_bg_fromm_url(url):
    try:
        st.markdown(
            f"""
            <style>
            .stApp{{
                background-image: url({url});
                background-attachment: fixed;
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        pass




remote_css("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Poppins:wght@600&display=swap")
local_css("utils/style.css")

def Title():
    st.markdown("", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3, 100, 3])
    greetings = col2.header('On the path to become a legendary botanist')
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
        <style> button {
        background-color: rgb(0, 0, 0);
        opacity: 0;
        margin-left: 50px;
        width: 10vw;
        height: 10vh;
        }
        </style>""", unsafe_allow_html=True)
    columns = st.columns((3, 3, 3))

    columns = st.columns((3, 3, 3))
    columns[1].title("")
    columns[1].title("")
    columns[1].write("\n")

    st.markdown("""
        <style> h2 {
        background-color: rgba(0, 0, 0, 0);
        opacity: 0;}
        </style>""", unsafe_allow_html=True)
    columns[1].header("-")
    columns[1].header("-")
    columns[1].header("-")
    columns[1].header("-")
    columns[1].header("-")
    columns[1].header("-")
    columns[1].header("-")


    button_pressed = columns[1].button('Let\'s get started!')
    st.markdown("", unsafe_allow_html=True)
    if button_pressed:
        switch_page("filter")

def div_intro():
    st.markdown("""
    <div style="background-image: url("https://cdn.discordapp.com/attachments/1067577269389885460/1071493257663623291/soil-suckers-homepage2.png") "background-color: lightblue; padding: 10px;">
        <p>This is a text element within a div.</p>
    </div>
    """, unsafe_allow_html=True)


def main():

    #Title()
    # calls the function to fetch the background
    add_bg_fromm_url(
        "https://cdn.discordapp.com/attachments/1067577269389885460/1071514005253927022/abou.png")
    goButton()
    #howItWorks()
    #userPropaganda()



if __name__ == '__main__':
    main()
