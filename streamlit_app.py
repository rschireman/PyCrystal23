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
    toldee = st.sidebar.selectbox('TOLDEE', ('6', '8', '10', '11', '12'), index=1)
    tolinteg = st.sidebar.selectbox('TOLINTEG', ('7 7 7 7 14', '8 8 8 8 16', '9 9 9 9 18', '10 10 10 10 20', '10 10 10 15 30'))
    dispersion = st.sidebar.selectbox('Dispersion', (True, False),)
    shrink = st.sidebar.selectbox('SHRINK', ('2 2', '4 4', '6 6', '8 8', '10 10', '12 12'))
    uploaded_file = st.file_uploader("Upload Structure File", accept_multiple_files=False)
    if uploaded_file:
        structures = input_generator.get_structures(uploaded_file)
        basis_references = input_generator.get_basis_references(user_basis_set, structures)
        

        input_dict['user_basis'] = user_basis_set
        input_dict['functional'] = user_functional
        input_dict['structures'] = structures
        input_dict['calc_type'] = calc_type
        input_dict['toldee'] = toldee
        input_dict['tolinteg'] = tolinteg
        input_dict['dispersion'] = dispersion
        input_dict['shrink'] = shrink

        input = input_generator.write_input(input_dict=input_dict)
        st.text_area(label="INPUT File", value=input, height=350)
        st.text_area(label="References (bibtext format)", value=basis_references)
    
