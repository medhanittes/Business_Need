import os
from dotenv import load_dotenv


#to load environment variable
load_dotenv()

#to fetch database connection parameters from environment variables
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
DB_PORT = os.getenv("DB_PORT").strip()
print("DB_PORT:", DB_PORT)