import streamlit as st
import basis_set_exchange as bse
from database.connection import  query_basis_individual_atoms
import periodictable



st.set_page_config(
        page_title="CRYSTAL Basis Sets",
        page_icon='U+269B',
        layout='wide',
        initial_sidebar_state='expanded'
    )



st.title('CRYSTAL Basis Sets')

atom = st.selectbox("Atom", periodictable.elements[1::])

all_basis_sets = bse.get_all_basis_names()
user_basis_set = st.sidebar.selectbox("Basis Set", all_basis_sets, index=33)

result = query_basis_individual_atoms(user_basis_set, atom)