from supabase import create_client, Client
import os

def test_connection():

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)


    response = supabase.table('CrystalBasisData').select('basis_data').match({'element': 'O', 'basis': '6-311G(d,p)'}).execute()
    print(response.data[0]['basis_data'])