import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

#to load environment variable
load_dotenv()

#to fetch database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT =os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER =os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def load_data_from_postgres(query):
    try:
        connection = psycopg2.connect(
           host=DB_HOST, 
           port=DB_PORT,
           databas=DB_NAME,
           user=DB_USER,
           password=DB_PASSWORD
        )
        #to load data using panda
        df = pd.read_sql_query(query, connection)
        #to close the database connection
        connection.close()
        
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None