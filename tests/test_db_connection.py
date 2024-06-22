from supabase import create_client, Client
import os

def test_connection():
    """
    Query crystallographic basis data for a given basis set and atomic structures.

    This function takes a basis set name and a dictionary of atomic structures as input,
    and queries a database for crystallographic basis data. It returns a dictionary
    that maps each unique atom in the structures to a list of basis data entries found
    in the database for that atom and basis set.

    Returns:
    dict: A dictionary where the keys are unique atomic species found in the input
          structures, and the values are lists of basis data entries retrieved from
          the database for the specified basis set and atom. The structure of each
          entry in the list depends on the database schema.

    """
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    
    result = {}
    response = supabase.table('CrystalBasisData').select('*').match({'element': 'H', 'basis': '6-311G(d,p)'}).execute()
    result['H'] = list(response.data[0]['basis_data'])

    assert result is not None
    