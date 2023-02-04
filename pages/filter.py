from service.locateService import *
import streamlit as st

# Store the initial value of widgets in session state
st.session_state.placeholder = "Boston"
st.session_state.disabled = False

# form
# form = st.form(key="form_settings")
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.caption("Preference")
    purpose = st.selectbox("Select your purpose",
                           ('Food (vegetables & fruit)',
                            'Decoration (plants & flowers)',
                            'Both'),
                           label_visibility='collapsed')

    submitted = st.button("search")

with col2:
    st.caption("Allergy")
    allergy = st.selectbox("Select",
                           ('1',
                            '2',
                            '3'),
                           label_visibility='collapsed')

with col3:
    st.session_state.disabled = st.checkbox("locate me")
    if st.session_state.disabled:
        ip = get_ip()
        address, _, _ = get_location(ip)
        st.session_state.placeholder = address
    address = col3.text_input(
        "City",
        label_visibility="collapsed",
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
        value=st.session_state.placeholder
    )

