import streamlit as st
import pymongo
import basis_set_exchange as bse

ALL_BASIS_SETS = bse.get_all_basis_names()
print(ALL_BASIS_SETS)

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

# Pull data from the collection.
@st.cache_data(ttl=10)
def query_basis(basis_set, _structures):
    db = client.CrystalBasisData
    result = {}
    for key,value in _structures.items():
        atoms = set(value.get_chemical_symbols())
        for atom in atoms:
            items = db.basis_data.find({"Basis Set": basis_set, "atom": atom})
            result[atom] = list(items)
    return result

