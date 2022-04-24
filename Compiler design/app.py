import numpy as np
import streamlit as st
import inter
PAGES = {
    'Intermediate code generator':inter
}

st.sidebar.title('Mental Harmony')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()