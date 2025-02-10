from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db():
    # Get the MongoDB URI from environment variable
    mongo_uri = os.getenv('MONGO_URI')
    
    if not mongo_uri:
        raise ValueError("MongoDB URI is not set in the .env file")
    
    # Create the client and access the database
    client = MongoClient(mongo_uri)
    db = client['pdf_data_db'] 
    return db
