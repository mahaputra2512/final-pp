import streamlit as st
from overview_page import overview_page
from cataract_info_page import cataract_info_page
from dataset_page import dataset_page
from prediction_page import prediction_page

# Set page configuration and styling
st.set_page_config(page_title="Cataract Prediction App", page_icon=":eyes:", layout="wide")

# Create navigation bar
pages = {
    "Overview": overview_page,
    "Cataract Information": cataract_info_page,
    "Dataset Information": dataset_page,
    "Prediction": prediction_page
}

# Sidebar navigation
page = st.sidebar.selectbox("Select a page", tuple(pages.keys()))

# Display selected page
pages[page]()
