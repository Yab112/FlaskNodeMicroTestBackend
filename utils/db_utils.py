from pymongo import MongoClient
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_db():
    mongo_uri = os.getenv('MONGO_URI')
    if not mongo_uri:
        raise ValueError("MongoDB URI is not set in the .env file")
    
    logging.info(f"Connecting to MongoDB with URI: {mongo_uri}")
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=50000)
    db = client['pdf_data_db']
    return db

def store_data(collection_name, data):
    db = get_db()
    collection = db[collection_name]
    collection.insert_one(data)
    print(f"Data successfully stored in {collection_name}")
