import mysql.connector

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(
            host="",
            user="",
            password="",
            database=""
        )
        if connection.is_connected():
            print("✓ Database connection successful")
            return connection
    except mysql.connector.Error as err:
        print(f"✗ Connection error: {err}")
        return None

db_connection = get_db_connection()