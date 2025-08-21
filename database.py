from pymongo import MongoClient
import os

MONGO_PSWD = os.getenv("MONGO_PSWD")
MONGO_URL = "mongodb+srv://Dimple:mongo123@cluster0.eb6crsc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URL)
db = client.pingwire_db
user_collection = db.users
messages_collection = db.messages

