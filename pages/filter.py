import streamlit
from streamlit_extras.switch_page_button import switch_page

from service.locateService import *
from streamlit_image_select import image_select
from utils.st import *
from utils.serach_algorithm import *

# set up page configuration
st.set_page_config(
    page_title="plant gallery", page_icon="🍃",
    initial_sidebar_state="collapsed",
    layout="wide"
)
remote_css(
    "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family"
    "=Poppins:wght@600&display=swap")
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

# Store the initial value in session state
st.session_state.placeholder = "Boston"
st.session_state.disabled = False

# load Json & initialize picture gallery
with open("./data/plant_info/example.json", "r") as f:
    EXAMPLES = json.load(f)
file_pattern = "data/plant_pics/{}.png"

if "plant_name" not in st.session_state.keys():
    st.session_state.plant_name = list(EXAMPLES.keys())[:4]
    st.session_state.plant_fp = \
        [file_pattern.format(name.lower())
         for name in st.session_state.plant_name]
name_selected = st.session_state.plant_name[0]
st.session_state["previous_example_index"] = 0
plant = EXAMPLES[name_selected].copy()
st.session_state.Description = plant["Description"]

# Page title
st.markdown("# _Plant Gallery_")

# filter form
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.caption("Preference")
    purpose = st.selectbox("Select your purpose",
                           ('Decoration',
                            'Edible',
                            'Both'),
                           label_visibility='collapsed')
    search = st.button("Submit")

with col2:
    st.caption("Allergy")
    allergy = st.selectbox("Select",
                           ('Pollen',
                            'Wheat',
                            'Chili'),
                           label_visibility='collapsed')

with col3:
    st.session_state.disabled = st.checkbox("locate me")
    if st.session_state.disabled:
        ip = get_ip()
        address = get_location(ip)
        st.session_state.placeholder = address

    address = col3.text_input(
        "City",
        label_visibility="collapsed",
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
        value=st.session_state.placeholder
    )

# actions after user clicks the search button
if search:
    plant_name = search_plant(EXAMPLES, address, purpose)
    plant_fp = get_image_path(plant_name)
    st.session_state.plant_name = plant_name
    st.session_state.plant_fp = plant_fp

# actions after user selected any image
index_selected = image_select(
    "",
    images=st.session_state.plant_fp,
    captions=st.session_state.plant_name,
    index=0,
    return_value="index",
)

# update the index in the session_state
if index_selected != st.session_state["previous_example_index"] or search:
    st.session_state.plant_name = st.session_state.plant_name
    st.session_state.plant_fp = st.session_state.plant_fp

    name_selected = st.session_state.plant_name[index_selected]
    plant = EXAMPLES[name_selected].copy()
    st.session_state.Description = plant["Description"]
    st.session_state["previous_example_index"] = index_selected

st.markdown("<t1>"+st.session_state["Description"]+"</t1>", unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    if st.button("Visualize Me 🌷"):
        switch_page("visual_garden")

with col5:
    if st.button("Soil Test 🔬"):
        switch_page("userForm")
