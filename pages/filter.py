from service.locateService import *
import streamlit as st
from streamlit_image_select import image_select

st.set_page_config(
    page_title="plant gallery", page_icon="🍃",
    initial_sidebar_state="collapsed")
st.markdown("# Plant Gallery")

# Store the initial value of widgets in session state
st.session_state.placeholder = "Boston"
st.session_state.disabled = False

# form
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.caption("Preference")
    purpose = st.selectbox("Select your purpose",
                           ('Food (vegetables & fruit)',
                            'Decoration (data & flowers)',
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

example_image_pattern = "data/plant_pics/{}.png"
EXAMPLES = ["tomato", "potato", "onion", "strawberry"]
example_image_fp = [
    example_image_pattern.format(name.lower()) for name in EXAMPLES[:4]
]
index_selected = image_select(
    "",
    images=example_image_fp,
    captions=EXAMPLES[:4],
    index=0,
    return_value="index",
)
if index_selected != st.session_state["previous_example_index"]:
    name_selected = EXAMPLES[index_selected]
    st.session_state.update(EXAMPLES[name_selected].copy())
    st.session_state["previous_example_index"] = index_selected

