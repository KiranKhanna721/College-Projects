import numpy as np
import streamlit as st
import covid
import mental

PAGES = {
    "Mental healthcare chatbot": mental ,
    "Covid heakthcare chatbot": covid 
}

st.sidebar.title('Chatbot')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()