import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),          # Correctly retrieve the host
        user=os.getenv('DB_USER'),          # Correctly retrieve the user
        password=os.getenv('DB_PASSWORD'),  # Correctly retrieve the password
        database=os.getenv('DB_DATABASE'),  # Correctly retrieve the database name
        port=3306
    )
