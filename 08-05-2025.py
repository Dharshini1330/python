from pymongo import MongoClient
connection=MongoClient("mongodb://localhost:27017")
print("connected")
db= connection["students_id"]
print("db created")
collection = db["class"]
print("collection is created")
collection.insert_one({"name":"adwik","class":"a"})
print("data inserted")


