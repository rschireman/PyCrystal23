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

ELEMENTS =  [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]



atom = st.selectbox("Atom", ELEMENTS)

all_basis_sets = bse.get_all_basis_names()
user_basis_set = st.sidebar.selectbox("Basis Set Data", all_basis_sets, index=33)

result = query_basis_individual_atoms(user_basis_set, atom)

basis_references = bse.get_references(user_basis_set, elements=atom, fmt='bib')

st.text_area(label='Basis Data', value=''.join(result[atom]), height=500)
st.text_area(label="References", value=basis_references, height=300)