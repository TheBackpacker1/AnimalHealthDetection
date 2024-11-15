from pymongo import MongoClient

mongo_uri ="mongodb+srv://mohamedlouati002:HDFMzGC3KTs56vJR@cluster0.62oql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client_mongo=MongoClient(mongo_uri )
db=client_mongo["AHDProject0"]
SensorDatacollection=db["SensorData"]
User_Collection=db["UserCollection"]


