import streamlit as st

# set basic page config
st.set_page_config(page_title="PyCRYSTAL23",
                    page_icon='U+269B',
                    layout='wide',
                    initial_sidebar_state='expanded')

from utils import input_generator
from database import connection

if __name__ == "__main__":
    st.title('PyCRYSTAL23')
    st.markdown("""
        PyCRYSTAL23 is a user-friendly Python tool designed to help generate CRYSTAL23 input files with ease. 
        Whether you're a seasoned materials scientist or just starting with CRYSTAL23, this tool provides a simple and intuitive interface, 
        letting you focus on the science.
        ---
        """, unsafe_allow_html=True)

    user_bais_set = st.sidebar.text_input("Basis Set")
    
    user_functional = st.sidebar.selectbox("Functional", ('B3LYP', 'PBE', 'PBE0', 'BLYP', 
                                                   'PBESOL'))
   
    basis_set = st.sidebar.write("Calculation Type (select one)")
    uploaded_files = st.file_uploader("Upload Structure File(s)", accept_multiple_files=True)
    structures = input_generator.get_structures(uploaded_files)
    
    st.text_area(label="INPUT File", value='', height=350)
    st.text_area(label="References",)
    
    