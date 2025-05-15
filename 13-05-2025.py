##from pymongo import MongoClient
##
##connection = MongoClient("mongodb://localhost:27017/")
##print("Connection established Successfully...")
##
##db = connection["Office"]
##print("Database created")
##
##collection = db["Employees"]
##print("Collection created")
##
### collection.insert_one({"_id": 3, "Name":"Dharshini", "Age": 19})
### print("data inserted")
##
### collection.insert_many( [
###     {"name": "Bob", "age": 32},
###     {"name": "Charlie", "age": 24}
### ])
##
### print(collection.find_one({"name": "Charlie"}))
##
### for doc in  collection.find():
###     print(doc)
##
### collection.update_many({"name":"Charlie"},{"$set":{"name":"Bob"}})
##
### collection.delete_many({"name":"Bob"})


from pymongo import MongoClient
connection=MongoClient("mongodb://localhost:27017/")
db=connection["namelist"]
collection=db["names"]
##collection.insert_one({"name":"aakash","age":7})
##collection.insert_many([{"name":"advik","age":13},{"name":"yadav","age":18}])
##collection.insert_many([{"name":"ruthran","age":15},{"name":"yuvan","age":20},{"name":"yathra","age":23},{"name":"yukitha","age":24}])
##print(collection.find_one({"name":"yathra"}))
##for Find in collection.find():
##    print(Find)
##collection.update_one({"name":"aakash"},{"$set":{"name":"ashwin"}})
##collection.update_many({"name":"aakash"},{"$set":{"name":"ashwin"}})
##collection.delete_one({"name":"ruthran"})
##collection.delete_many({"name":"ashwin"})
##collection.replace_one({"name": "yathra"}, {"name": "jp"})
##print(collection.count_documents({"age":{"$gt":19}})
print(collection.distinct("name"))
print("db created ")
