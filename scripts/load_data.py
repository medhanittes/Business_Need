import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

#to load environment variable
load_dotenv()

#to fetch database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def load_data_from_postgres(query):
    try:
        connection = psycopg2.connect(
           host=os.getenv("DB_HOST").strip(), 
           port=os.getenv("DB_PORT").strip(),
           dbname=os.getenv("DB_NAME").strip(),
           user=os.getenv("DB_USER").strip(),
           password=os.getenv("DB_PASSWORD").strip(),
        )
        #to load data using panda
        df = pd.read_sql_query(query, connection)
        #to close the database connection
        connection.close()
        
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def load_data_using_sqlalchemy(query):
    try:
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        df = pd.read_sql_query(query, engine)
        
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
