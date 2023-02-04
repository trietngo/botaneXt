from utils.st import *
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import base64
import streamlit as st

# st.title("_Thank you for applying for soil testing!_")
#
# st.markdown("""<style> css-10trblm e16nr0p30 {
#         color: #5c7457;
#         justify: center;
#     }
#     </style>
#     """, unsafe_allow_html=True)


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
            unsafe_allow_html= True
        )
    except:
        pass

def acknowledgements():

    st.header("YOUR SOIL SAMPLING REQUEST HAS NOW BEEN SUBMITTED.")

    st.markdown("""<style> h2 {
        max-width: 90vw;
        color: #5c7457;
        text-align: center;
        font-size: 4rem;
        font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    st.write("Thanks for taking the first step towards a greener future! ")
    st.write(
        "Your soil sample order shows your commitment to reducing your carbon footprint and making a positive impact on the environment. ")
    st.write("We're excited to be a part of your journey towards a sustainable lifestyle. Happy gardening!")

    st.markdown("""<style> p {
            max-width: 90vw;
            color: #5c7457;
            text-align: center;
            font-size: 1.5rem;
            font-weight: normal;
            }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("""<style> .css-91z34k {
        max-width: 70rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.image("https://media.discordapp.net/attachments/1067577269389885460/1071537269971882075/icons8-plant-100.png")

    st.markdown("""<style> .css-1kyxreq {
            justify-content: center;
        </style>
        """, unsafe_allow_html=True)

    st.markdown("""<style> img {
                margin-top: 30px;
            </style>
            """, unsafe_allow_html=True)

    st.write("Created by: **__Hua Wang, Senay Tilahun, Zadie Moon, Yan To, Huiqin Hu, and Triet Ngo__** ")

def main():
    acknowledgements()

main()