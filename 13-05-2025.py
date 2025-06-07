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
##print(collection.distinct("name"))
##print("db created ")
##📌 Query Operators
##Operator	Description	Example
##$eq	Equal to	{"age": {"$eq": 25}}
##$ne	Not equal to	{"name": {"$ne": "John"}}
##$gt	Greater than	{"age": {"$gt": 25}}
##$gte	Greater than or equal to	{"age": {"$gte": 25}}
##$lt	Less than	{"age": {"$lt": 25}}
##$lte	Less than or equal to	{"age": {"$lte": 25}}
##$in	Value is in list	{"name": {"$in": ["Alice", "Bob"]}}
##$nin	Value not in list	{"status": {"$nin": ["inactive", "banned"]}}
##$exists	Field exists or not	{"email": {"$exists": True}}
##$type	Match specific BSON type	{"score": {"$type": "double"}}
##$and	Logical AND	{"$and": [{"age": {"$gt": 20}}, {"active": True}]}
##$or	Logical OR	{"$or": [{"age": 30}, {"city": "Delhi"}]}
##$not	Logical NOT	{"age": {"$not": {"$gt": 25}}}
##$nor	Neither condition is true	{"$nor": [{"age": 30}, {"name": "Alice"}]}
##$all	All elements must match	{"tags": {"$all": ["mongodb", "python"]}}
##$size	Array has specific length	{"tags": {"$size": 3}}
##
##🔧 Update Operators
##Operator	Description	Example
##$set	Set field value	{"$set": {"name": "Ashwin"}}
##$unset	Remove field	{"$unset": {"age": ""}}
##$inc	Increment field	{"$inc": {"views": 1}}
##$mul	Multiply field	{"$mul": {"price": 1.1}}
##$rename	Rename field	{"$rename": {"username": "user_name"}}
##$push	Add item to array	{"$push": {"tags": "python"}}
##$pull	Remove item from array	{"$pull": {"tags": "old_tag"}}
##$addToSet	Add to array if not present	{"$addToSet": {"tags": "unique_tag"}}
##$pop	Remove first/last array element	{"$pop": {"tags": 1}}
##$min	Set to min value if lower	{"$min": {"score": 50}}
##$max	Set to max value if higher	{"$max": {"score": 90}}
##$currentDate	Set field to current date	{"$currentDate": {"lastModified": True}}
##
