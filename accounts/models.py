from pymongo import MongoClient
from bson.objectid import ObjectId


from MongoConnection import User_Collection
# Connect to MongoDB


class User:
    def __init__(self, email, password, is_admin=False, user_id=None):
        self.user_id = user_id if user_id else str(ObjectId())  # MongoDB's ObjectId
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def save(self):
        user_data = {
            "user_id": self.user_id,
            "email": self.email,
            "password": self.password,
            "is_admin": self.is_admin
        }
        User_Collection.insert_one(user_data)

    @classmethod
    def find_by_email(cls, email):
        user_data = User_Collection.find_one({"email": email})
        if user_data:
            return cls(**user_data)
        return None

    @classmethod
    def update(cls, email, new_email=None, new_password=None):
        updates = {}
        if new_email:
            updates['email'] = new_email
        if new_password:
            updates['password'] = new_password
        if updates:
            User_Collection.update_one({"email": email}, {"$set": updates})

    @classmethod
    def delete(cls, email):
        User_Collection.delete_one({"email": email})
