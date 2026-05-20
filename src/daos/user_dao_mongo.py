"""
User DAO (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId
from models.user import User

class UserDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)
            db_host = os.getenv("MONGODB_HOST")
            db_name = os.getenv("MONGODB_DB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")
            print(f"DEBUG: host={db_host}, db={db_name}, user={db_user}")  # ← voir les valeurs    
            self.client = MongoClient(host=db_host,port=27017 ,username=db_user, password=db_pass) 
            self.db = self.client[db_name]
            self.collection = self.db["users"]
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        users = []
        for doc in self.collection.find():
            users.append(User(
                user_id = str(doc["_id"]),
                name    = doc["name"],
                email   = doc["email"]
            ))
        return users

    def insert(self, user):
        """ Insert given user into MongoDB """
        doc = {"name": user.name, "email": user.email}
        result = self.collection.insert_one(doc)
        return str(result.inserted_id)

    def update(self, user):
        """ Update given user in MongoDB """
        self.collection.update_one(
            {"_id": ObjectId(user.id)},
            {"$set": {"name": user.name, "email": user.email}}
        )

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        self.collection.delete_one({"_id": ObjectId(user_id)})

    def delete_all(self):
        """ Empty users collection in MongoDB """
        self.collection.delete_many({})

    def close(self):
        self.client.close()
