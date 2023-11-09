import pytest
from database import connection

def test_database_connection():
    try:
        # Attempt to connect to the database
        db_connection = connection.init_connection()
        db = db_connection.mydb
        # Check if the connection is successful
        assert db.command("ping") == {'ok': 1.0}
    except Exception as e:
        pytest.fail(f"Failed to connect to the database: {str(e)}")