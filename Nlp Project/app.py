import numpy as np
import streamlit as st
import covid
import mental
import ca
import ca1
PAGES = {
    "Mental healthcare chatbot": mental ,
    "Covid heakthcare chatbot": covid ,
    "Condition prediction":ca ,
    "Sentimental Analysis":ca1
}

st.sidebar.title('Chatbot')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()