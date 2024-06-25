import streamlit as st
import basis_set_exchange as bse

st.set_page_config(
        page_title="CRYSTAL Basis Sets",
        page_icon='U+269B',
        layout='wide',
        initial_sidebar_state='expanded'
    )

st.title('CRYSTAL Basis Sets')

all_basis_sets = bse.get_all_basis_names()
user_basis_set = st.sidebar.selectbox("Basis Set", all_basis_sets, index=33)