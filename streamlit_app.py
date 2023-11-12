import streamlit as st
import basis_set_exchange as bse



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

    input_dict = {}

    ALL_BASIS_SETS = bse.get_all_basis_names()
    user_basis_set = st.sidebar.selectbox("Basis Set", ALL_BASIS_SETS, index=33)
    
    user_functional = st.sidebar.selectbox("Functional", ('B3LYP', 'PBE', 'PBE0', 'BLYP', 
                                                   'PBESOL'))
   
    calc_type = st.sidebar.selectbox("Calculation Type", ('Single Point Energy', 'Geometry Optimization', 'Vibrational Frequencies', 'Equation of State'))
    uploaded_files = st.file_uploader("Upload Structure File(s)", accept_multiple_files=True)
    structures = input_generator.get_structures(uploaded_files)
    basis_references = input_generator.get_basis_references(user_basis_set, structures)

    input_dict['user_basis'] = user_basis_set
    input_dict['functional'] = user_functional
    input_dict['structures'] = structures
    input_dict['calc_type'] = calc_type

    input = input_generator.write_input(input_dict=input_dict)
    st.text_area(label="INPUT File", value=input, height=350)
    st.text_area(label="References (bibtext format)", value=basis_references)
    
