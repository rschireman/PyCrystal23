import streamlit as st
import pymongo

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()


def query_basis(basis_set, _structures):
    """
    Query crystallographic basis data for a given basis set and atomic structures.

    This function takes a basis set name and a dictionary of atomic structures as input,
    and queries a database for crystallographic basis data. It returns a dictionary
    that maps each unique atom in the structures to a list of basis data entries found
    in the database for that atom and basis set.

    Parameters:
    basis_set (str): The name of the basis set to query.
    _structures (dict): A dictionary of atomic structures where the keys are structure
                       identifiers and the values are objects containing information
                       about atomic species and positions.

    Returns:
    dict: A dictionary where the keys are unique atomic species found in the input
          structures, and the values are lists of basis data entries retrieved from
          the database for the specified basis set and atom. The structure of each
          entry in the list depends on the database schema.

    Example:
    basis_set = "6-311G(d,p)"
    structures = {
        "structure1": StructureObject1,
        "structure2": StructureObject2,
        # ... (more structures)
    }
    basis_data = query_basis(basis_set, structures)
    print(basis_data)
    # Output: {'H': [BasisDataEntry1, BasisDataEntry2], 'O': [BasisDataEntry3, BasisDataEntry4], ...}
    """
    db = client.CrystalBasisData
    result = {}
    for key,value in _structures.items():
        atoms = set(value.get_chemical_symbols())
        for atom in atoms:
            items = db.basis_data.find({"Basis Set": basis_set, "atom": atom})
            result[atom] = list(items)
    print(result)        
    return result

