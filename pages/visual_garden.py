import streamlit as st

greetings = st.title('_Flora / Edible Selected: Roses_')
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    before = col1.header("_Before_")    
    beforeImage = col1.image("https://st2.depositphotos.com/1010683/9547/i/950/depositphotos_95478192-stock-photo-beautiful-empty-garden.jpg", width= 300)


with col2:  
    after = col3.header("_After_")
    afterImage = col3.image("https://www.youredm.com/wp-content/uploads/2021/05/nurture-flipped.jpg", width= 300)


st.markdown("""<style> .css-po3vlj exg6vvm15 {
        width: 0;
        height: 0;
    }
    """, unsafe_allow_html=True)

st.header("_See it Before You Sow It_") 
st.write("Use our virtual try-on feature to get a glimpse of what your garden could look like with our AI-powered visualization tool"
)

st.file_uploader("_Upload your garden here_")
st.write("_Privacy Notice: By using our app, you understand and agree that any images provided will only be used for the purpose of generating a virtual representation of your garden using our AI model. We will not save any images or use them for any other purpose. Your privacy and security are of utmost importance to us_")