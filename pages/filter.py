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

# Store the initial value in session state
st.session_state.placeholder = "Boston"
st.session_state.disabled = False

# load Json & initialize picture gallery
with open("./data/plant_info/example.json", "r") as f:
    EXAMPLES = json.load(f)
file_pattern = "data/plant_pics/{}.png"
if "plane_name" not in st.session_state.keys():
    plant_name = list(EXAMPLES.keys())[:4]
    plant_fp = [file_pattern.format(name.lower()) for name in plant_name]
    name_selected = plant_name[0]
    st.session_state["previous_example_index"] = 0
    st.session_state.update(EXAMPLES[name_selected].copy())
    st.session_state.plant_name = list(EXAMPLES.keys())[:4]
else:
    plant_name = st.session_state.plant_name
    plant_fp = get_image_path(plant_name)

# Page title
st.markdown("# Plant Gallery")

# filter form
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.caption("Preference")
    purpose = st.selectbox("Select your purpose",
                           ('Edible',
                            'Decoration',
                            'Both'),
                           label_visibility='collapsed')
    search = st.button("Submit")

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
    plant_name = search_plant(EXAMPLES, location, purpose)
    plant_fp = get_image_path(plant_name)
    st.session_state.plant_name = plant_name

# actions after user selected any image
index_selected = image_select(
    "",
    images=plant_fp,
    captions=plant_name,
    index=0,
    return_value="index",
)

# update the index in the session_state
if index_selected != st.session_state["previous_example_index"]:
    name_selected = plant_name[index_selected]
    st.session_state.update(EXAMPLES[name_selected].copy())
    st.session_state["previous_example_index"] = index_selected

with st.expander("See details", expanded=True):
    st.markdown(st.session_state["Description"], unsafe_allow_html=True)
