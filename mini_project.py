from pymongo import MongoClient

    
connection = MongoClient("mongodb://localhost:27017/")
db = connection["mini_task"]
collection = db["age_calculator"]  

print("Connection accomplished successfully")

try:
    name = input("Enter your name: ")
    birthyear = int(input("Enter your birth year: "))
    current_age = 2025 - birthyear

   
    collection.insert_one({
        "name": name,
        "birthyear": birthyear,
        "age": current_age
    })

except ValueError:
    print("Please enter a valid number for the birth year.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Data operation completed.")
