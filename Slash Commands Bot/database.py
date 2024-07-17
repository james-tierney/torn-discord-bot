import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print(f"Connected to {DB_NAME} database on PostgreSQL on port {DB_PORT}")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")

def execute_query(query, params=None):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

def fetch_query(query, params=None):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(query, params)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def test_insert_data():
    query = """
    INSERT INTO user_stats (discord_id, last_call, strength, speed, defense, dexterity, total)
    VALUES (%s, current_timestamp, %s, %s, %s, %s, %s)
    """
    params = ("discord_user_id", 100, 120, 80, 150, 450)  # Replace with actual data
    execute_query(query, params)
    print("Dummy data inserted successfully!")

# Example usage
if __name__ == "__main__":
    connection = connect_to_db()
    
    # Test insert operation
    test_insert_data()

    # Close the connection when done
    if connection:
        connection.close()
        print("PostgreSQL connection is closed")