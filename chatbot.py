######from pymongo import MongoClient
######
####### MongoDB setup
######connection = MongoClient("mongodb://localhost:27017")
######print("Connected to MongoDB")
######db = connection["user"]
######collection = db["usermangement"]
######print("Database and collection ready")
####collection.insert_one({"_id":1,"username":"adwik","password":"1234567890","role":"user","email":"adwik3@gmail.com","phone":9874561230,"age":25})
####collection.insert_one({"_id":2,"username":"joshua","password":"1234567890","role":"admin","email":"joshua@gmail.com","phone":9245678016,"age":21})
####collection.insert_one({"_id":3,"username":"jayapriyan","password":"1234567890","role":"superadmin","email":"jayapriyan30@gmail.com","phone":8122567465,"age":19})
####collection.insert_one({"_id":4,"username":"yasodha","password":"1234567890","role":"admin","email":"yasodha43@gmail.com","phone":7123647895,"age":22})
####collection.insert_one({"_id":5,"username":"athira","password":"1234567890","role":"user","email":"athira@gmail.com","phone":8546712358,"age":22})
########
########
######## #Register a new user (default role: user)
######def newuser():
######    print("Register New User")
######    newusername = input("Enter a new username: ")
######    newpassword = input("Enter numeric password: ")
########    newrole= input("Enter your role: ")
######
######    if not newpassword.isdigit():
######        print("Password must contain only numbers.")
######        return None
######
######    if collection.find_one({"username": newusername}):
######        print("Username already exists.")
######        return None
######
######    collection.insert_one({
######        "username": newusername,
######        "password": newpassword,
########        "role": newrole
######    })
######    print("Registration successful!")
######    return "user"
######
######
####### Login for existing user
######def existinguser():
######    print("Login Existing User")
######    existingusername = input("Enter your username: ")
######    existingpassword = input("Enter your password: ")
######
######    user = collection.find_one({"username": existingusername})
######
######    if user:
######        if user["password"] == existingpassword:
######            print("Login successful.")
######            return user.get("role", "user") 
######        else:
######            print("Incorrect password.")
######            return None
######    else:
######        print("User not found.")
######        return None
######
######
####### Combined authentication handler
######def authenticate():
######    choice = input("Are you a new user? (yes/no): ").lower()
######
######    if choice == "yes":
######        return newuser()  # returns role
######    elif choice == "no":
######        return existinguser()  # returns role if login successful
######    else:
######        print("Invalid input. Please type 'yes' or 'no'.")
######        return None
######
######
####### User function
######def user():
######    username = input("Enter your username to get details: ")
######    user_doc = collection.find_one({"username": username})
########    password change and they can edit thier names
######    if user_doc:
######        print("User found:")
######        print(user_doc)
######    else:
######        print("User not found.")
######
######
####### Add a user (admin/superadmin)
######def add_user():
######    print("Add New User")
######    newusername = input("Enter new username: ")
######    newpassword = input("Enter numeric password: ")
######    role = input("Enter role (user/admin/superadmin): ").lower()
########if super admin exists admin cannot able to view it.block and unblock from both admin and superadmin ,super admin can change the password .
######    if not newpassword.isdigit():
######        print("Password must contain only numbers.")
######        return
######    if collection.find_one({"username": newusername}):
######        print("Username already exists.")
######        return
######
######    collection.insert_one({
######        "username": newusername,
######        "password": newpassword,
######        "role": role
######    })
######    print("User added successfully.")
######
######
####### Delete a user
######def delete_user():
######    username = input("Enter username to delete: ")
######    result = collection.delete_one({"username": username})
######    if result.deleted_count > 0:
######        print("User deleted.")
######    else:
######        print("User not found.")
######
######
####### View all users
######def view_users():
######    print("All users:")
######    for doc in collection.find():
######        print(doc)
######
######
####### Drop the entire collection (superadmin only)
######def drop_users():
######    confirm = input("Are you sure you want to drop the collection? (yes/no): ").lower()
######    if confirm == "yes":
######        collection.drop()
######        print("Collection dropped.")
######    else:
######        print("Collection not dropped.")
######
######
####### Admin interface
######def admin():
######    print("Welcome Admin!")
######    while True:
######        choice = input("Choose operation (add/delete/view/exit): ").lower()
######        if choice == "add":
######            add_user()
######        elif choice == "delete":
######            delete_user()
######        elif choice == "view":
######            
######            view_users()
######        elif choice == "exit":
######            break
######        else:
######            print("Invalid choice. Try again.")
######
######
####### Superadmin interface
######def superadmin():
######    print("Welcome Superadmin!")
######    while True:
######        choice = input("Choose operation (add/delete/view/drop/exit): ").lower()
######        if choice == "add":
######            add_user()
######        elif choice == "delete":
######            delete_user()
######        elif choice == "view":
######            view_users()
######        elif choice == "drop":
######            drop_users()
######        elif choice == "exit":
######            break
######        else:
######            print("Invalid choice. Try again.")
######
######
####### Main controller
######def main():
######    role = authenticate()
######
######    if role == "user":
######        user()
######    elif role == "admin":
######        admin()
######    elif role == "superadmin":
######        superadmin()
######    else:
######        print("Access Denied. Login/Registration failed.")
######
######
####### Entry point
######main()
####
####
####
####
####
####
####
####
####
####from pymongo import MongoClient
####
##### MongoDB setup
####connection = MongoClient("mongodb://localhost:27017")
####print("Connected to MongoDB")
####db = connection["user"]
####collection = db["usermangement"]
####print("Database and collection ready")
####
####
##### Register a new user (default role: user)
####def newuser():
####    print("Register New User")
####    newusername = input("Enter a new username: ")
####    newpassword = input("Enter numeric password: ")
####
####    if not newpassword.isdigit():
####        print("Password must contain only numbers.")
####        return None
####
####    if collection.find_one({"username": newusername}):
####        print("Username already exists.")
####        return None
####
####    collection.insert_one({
####        "username": newusername,
####        "password": newpassword,
####        "role": "user",
####        "is_blocked": False
####    })
####    print("Registration successful!")
####    return "user"
####
####
##### Login for existing user
####def existinguser():
####    print("Login Existing User")
####    existingusername = input("Enter your username: ")
####    existingpassword = input("Enter your password: ")
####
####    user = collection.find_one({"username": existingusername})
####
####    if user:
####        if user.get("is_blocked", False):
####            print("User is blocked. Contact admin.")
####            return None, None
####
####        if user["password"] == existingpassword:
####            print("Login successful.")
####            return user.get("role", "user"), user["username"]
####        else:
####            print("Incorrect password.")
####    else:
####        print("User not found.")
####    return None, None
####
####
##### Combined authentication handler
####def authenticate():
####    choice = input("Are you a new user? (yes/no): ").lower()
####
####    if choice == "yes":
####        role = newuser()
####        return role, None
####    elif choice == "no":
####        return existinguser()
####    else:
####        print("Invalid input. Please type 'yes' or 'no'.")
####        return None, None
####
####
##### USER 
####def user(username):
####    user_doc = collection.find_one({"username": username})
####    if user_doc:
####        print("Welcome,", user_doc["username"])
####        print("Your Details:", user_doc)
####        choice = input("Do you want to update your name or password? (name/password/none): ").lower()
####        if choice == "name":
####            new_name = input("Enter new username: ")
####            collection.update_one({"username": username}, {"$set": {"username": new_name}})
####            print("Name updated.")
####        elif choice == "password":
####            new_password = input("Enter new numeric password: ")
####            if new_password.isdigit():
####                collection.update_one({"username": username}, {"$set": {"password": new_password}})
####                print("Password updated.")
####            else:
####                print("Password must be numeric.")
####    else:
####        print("User not found.")
####
####
##### Add a user 
####def add_user():
####    print("Add New User")
####    newusername = input("Enter new username: ")
####    newpassword = input("Enter numeric password: ")
####    role = input("Enter role (user/admin/superadmin): ").lower()
####
####    if not newpassword.isdigit():
####        print("Password must contain only numbers.")
####        return
####    if collection.find_one({"username": newusername}):
####        print("Username already exists.")
####        return
####
####    collection.insert_one({
####        "username": newusername,
####        "password": newpassword,
####        "role": role,
####        "is_blocked": False
####    })
####    print("User added successfully.")
####
####
##### Delete a user
####def delete_user():
####    username = input("Enter username to delete: ")
####    result = collection.delete_one({"username": username})
####    if result.deleted_count > 0:
####        print("User deleted.")
####    else:
####        print("User not found.")
####
####
##### Edit a user's info
####def edit_user():
####    username = input("Enter username to edit: ")
####    user_doc = collection.find_one({"username": username})
####    if not user_doc:
####        print("User not found.")
####        return
####
####    new_username = input("Enter new username (leave blank to skip): ")
####    new_password = input("Enter new password (leave blank to skip): ")
####
####    update_fields = {}
####    if new_username:
####        update_fields["username"] = new_username
####    if new_password:
####        if new_password.isdigit():
####            update_fields["password"] = new_password
####        else:
####            print("Password must be numeric.")
####            return
####
####    if update_fields:
####        collection.update_one({"username": username}, {"$set": update_fields})
####        print("User updated successfully.")
####    else:
####        print("Nothing to update.")
####
####
##### Block or unblock 
####def block_unblock_user():
####    username = input("Enter username to block/unblock: ")
####    user_doc = collection.find_one({"username": username})
####    if user_doc:
####        current_status = user_doc.get("is_blocked", False)
####        new_status = not current_status
####        collection.update_one({"username": username}, {"$set": {"is_blocked": new_status}})
####        print(f"User {'blocked' if new_status else 'unblocked'} successfully.")
####    else:
####        print("User not found.")
####
####
##### View users
####def view_users(filter_out=None):
####    print("All Users:")
####    for doc in collection.find():
####        if filter_out and doc.get("role") == filter_out:
####            continue
####        print(doc)
####
####
##### Drop the entire collection 
####def drop_users():
####    confirm = input("Are you sure you want to drop the collection? (yes/no): ").lower()
####    if confirm == "yes":
####        collection.drop()
####        print("Collection dropped.")
####    else:
####        print("Collection not dropped.")
####
####
##### Admin 
####def admin():
####    print("Welcome Admin!")
####    while True:
####        choice = input("Choose operation (add/delete/edit/view/exit): ").lower()
####        if choice == "add":
####            add_user()
####        elif choice == "delete":
####            delete_user()
####        elif choice == "edit":
####            edit_user()
####        elif choice == "view":
####            view_users(filter_out="superadmin")
####        elif choice == "exit":
####            break
####        else:
####            print("Invalid choice. Try again.")
####
####
##### Superadmin 
####def superadmin():
####    print("Welcome Superadmin!")
####    while True:
####        choice = input("Choose operation (add/delete/edit/view/block/drop/exit): ").lower()
####        if choice == "add":
####            add_user()
####        elif choice == "delete":
####            delete_user()
####        elif choice == "edit":
####            edit_user()
####        elif choice == "view":
####            view_users()
####        elif choice == "block":
####            block_unblock_user()
####        elif choice == "drop":
####            drop_users()
####        elif choice == "exit":
####            break
####        else:
####            print("Invalid choice. Try again.")
####
####
##### Main 
####def main():
####    role, username = authenticate()
####
####    if role == "user":
####        user(username)
####    elif role == "admin":
####        admin()
####    elif role == "superadmin":
####        superadmin()
####    else:
####        print("Access Denied. Login/Registration failed.")
####
####
##### function call
####
####
####while(True):
####    main()
##
##
##
##
##
##
##
##
##
##
##
##
##
##from pymongo import MongoClient
##from tabulate import tabulate
##
### MongoDB setup
##connection = MongoClient("mongodb://localhost:27017")
##print("Connected to MongoDB")
##db = connection["user"]
##collection = db["usermangement"]
##print("Database and collection ready")
##
####collection.insert_one({"_id":1,"username":"adwik","password":"1234567890","role":"user","email":"adwik3@gmail.com","phone":9874561230,"age":25})
####collection.insert_one({"_id":2,"username":"joshua","password":"1234567890","role":"admin","email":"joshua@gmail.com","phone":9245678016,"age":21})
####collection.insert_one({"_id":3,"username":"jayapriyan","password":"1234567890","role":"superadmin","email":"jayapriyan30@gmail.com","phone":8122567465,"age":19})
####collection.insert_one({"_id":4,"username":"yasodha","password":"1234567890","role":"admin","email":"yasodha43@gmail.com","phone":7123647895,"age":22})
####collection.insert_one({"_id":5,"username":"athira","password":"1234567890","role":"user","email":"athira@gmail.com","phone":8546712358,"age":22})
##
##
##
### Register a new user (default role: user)
##def newuser():
##    print("Register New User")
##    newusername = input("Enter a new username: ")
##    newpassword = input("Enter numeric password: ")
##    email = input("Enter your email: ")
##    phone = input("Enter your phone number: ")
##    age = input("Enter your age: ")
##
##    if not newpassword.isdigit():
##        print("Password must contain only numbers.")
##        return None
##
##    if not phone.isdigit() or not age.isdigit():
##        print("Phone and Age must be numeric.")
##        return None
##
##    if collection.find_one({"username": newusername}):
##        print("Username already exists.")
##        return None
##
##    collection.insert_one({
##        "username": newusername,
##        "password": newpassword,
##        "email": email,
##        "phone": phone,
##        "age": int(age),
##        "role": "user",
##        "is_blocked": False
##    })
##    print("Registration successful!")
##    return "user"
##
##
### Login for existing user
##def existinguser():
##    print("Login Existing User")
##    existingusername = input("Enter your username: ")
##    existingpassword = input("Enter your password: ")
##
##    user = collection.find_one({"username": existingusername})
##
##    if user:
##        if user.get("is_blocked", False):
##            print("User is blocked. Contact admin.")
##            return None, None
##
##        if user["password"] == existingpassword:
##            print("Login successful.")
##            return user.get("role", "user"), user["username"]
##        else:
##            print("Incorrect password.")
##    else:
##        print("User not found.")
##    return None, None
##
##
### Combined authentication handler
##def authenticate():
##    choice = input("Are you a new user? (yes/no): ").lower()
##
##    if choice == "yes":
##        role = newuser()
##        return role, None
##    elif choice == "no":
##        return existinguser()
##    else:
##        print("Invalid input. Please type 'yes' or 'no'.")
##        return None, None
##
##
### USER ROLE
##def user(username):
##    user_doc = collection.find_one({"username": username})
##    if user_doc:
##        print("Welcome,", user_doc["username"])
##        print("Your Details:", user_doc)
##        choice = input("Do you want to update your (name/password/email/phone/age/none)? ").lower()
##        update_fields = {}
##
##        if choice == "name":
##            new_name = input("Enter new username: ")
##            update_fields["username"] = new_name
##        elif choice == "password":
##            new_password = input("Enter new numeric password: ")
##            if new_password.isdigit():
##                update_fields["password"] = new_password
##            else:
##                print("Password must be numeric.")
##        elif choice == "email":
##            new_email = input("Enter new email: ")
##            update_fields["email"] = new_email
##        elif choice == "phone":
##            new_phone = input("Enter new phone number: ")
##            if new_phone.isdigit():
##                update_fields["phone"] = new_phone
##            else:
##                print("Phone must be numeric.")
##        elif choice == "age":
##            new_age = input("Enter new age: ")
##            if new_age.isdigit():
##                update_fields["age"] = int(new_age)
##            else:
##                print("Age must be numeric.")
##
##        if update_fields:
##            collection.update_one({"username": username}, {"$set": update_fields})
##            print("Details updated.")
##    else:
##        print("User not found.")
##
##
### ADMIN & SUPERADMIN FUNCTIONS
##def add_user():
##    print("Add New User")
##    newusername = input("Enter new username: ")
##    newpassword = input("Enter numeric password: ")
##    email = input("Enter email: ")
##    phone = input("Enter phone number: ")
##    age = input("Enter age: ")
##    role = input("Enter role (user/admin/superadmin): ").lower()
##
##    if not newpassword.isdigit() or not phone.isdigit() or not age.isdigit():
##        print("Password, phone, and age must be numeric.")
##        return
##    if collection.find_one({"username": newusername}):
##        print("Username already exists.")
##        return
##
##    collection.insert_one({
##        "username": newusername,
##        "password": newpassword,
##        "email": email,
##        "phone": phone,
##        "age": int(age),
##        "role": role,
##        "is_blocked": False
##    })
##    print("User added successfully.")
##
##
##def delete_user():
##    username = input("Enter username to delete: ")
##    user_doc = collection.find_one({"username": username})
##    if user_doc and user_doc["role"] == "superadmin":
##        print("You cannot delete a superadmin.")
##        return
##    result = collection.delete_one({"username": username})
##    print("User deleted." if result.deleted_count > 0 else "User not found.")
##
##
##def edit_user():
##    username = input("Enter username to edit: ")
##    user_doc = collection.find_one({"username": username})
##    if not user_doc:
##        print("User not found.")
##        return
##    if user_doc["role"] == "superadmin":
##        print("You cannot modify a superadmin.")
##        return
##
##    print("Leave field blank to skip.")
##    new_username = input("New username: ")
##    new_password = input("New password: ")
##    new_email = input("New email: ")
##    new_phone = input("New phone: ")
##    new_age = input("New age: ")
##
##    update_fields = {}
##    if new_username:
##        update_fields["username"] = new_username
##    if new_password:
##        if new_password.isdigit():
##            update_fields["password"] = new_password
##        else:
##            print("Password must be numeric.")
##            return
##    if new_email:
##        update_fields["email"] = new_email
##    if new_phone:
##        if new_phone.isdigit():
##            update_fields["phone"] = new_phone
##        else:
##            print("Phone must be numeric.")
##            return
##    if new_age:
##        if new_age.isdigit():
##            update_fields["age"] = int(new_age)
##        else:
##            print("Age must be numeric.")
##            return
##
##    if update_fields:
##        collection.update_one({"username": username}, {"$set": update_fields})
##        print("User updated successfully.")
##    else:
##        print("Nothing to update.")
##
##
##def block_unblock_user():
##    username = input("Enter username to block/unblock: ")
##    user_doc = collection.find_one({"username": username})
##    if user_doc:
##        if user_doc["role"] == "superadmin":
##            print("You cannot block a superadmin.")
##            return
##        new_status = not user_doc.get("is_blocked", False)
##        collection.update_one({"username": username}, {"$set": {"is_blocked": new_status}})
##        print(f"User {'blocked' if new_status else 'unblocked'} successfully.")
##    else:
##        print("User not found.")
##
##
### VIEW USERS in TABLE
##def view_users(filter_out=None):
##    print("\n User Details Table:")
##    headers = ["Username", "Email", "Phone", "Age", "Role", "Blocked"]
##    table_data = []
##
##    for doc in collection.find():
##        if filter_out and doc.get("role") == filter_out:
##            continue
##        row = [
##            doc.get("username", ""),
##            doc.get("email", ""),
##            doc.get("phone", ""),
##            doc.get("age", ""),
##            doc.get("role", ""),
##            "Yes" if doc.get("is_blocked", False) else "No"
##        ]
##        table_data.append(row)
##
##    if table_data:
##        print(tabulate(table_data, headers=headers, tablefmt="grid"))
##    else:
##        print("No users to display.")
##
##
##def drop_users():
##    confirm = input("Are you sure you want to drop the collection? (yes/no): ").lower()
##    if confirm == "yes":
##        collection.drop()
##        print("Collection dropped.")
##    else:
##        print("Cancelled.")
##
##
### ADMIN ROLE
##def admin():
##    print("Welcome Admin!")
##    while True:
##        choice = input("Choose operation (add/delete/edit/view/exit): ").lower()
##        if choice == "add":
##            add_user()
##        elif choice == "delete":
##            delete_user()
##        elif choice == "edit":
##            edit_user()
##        elif choice == "view":
##            view_users(filter_out="superadmin")
##        elif choice == "exit":
##            break
##        else:
##            print("Invalid choice. Try again.")
##
##
### SUPERADMIN ROLE
##def superadmin():
##    print("Welcome Superadmin!")
##    while True:
##        choice = input("Choose operation (add/delete/edit/view/block/drop/exit): ").lower()
##        if choice == "add":
##            add_user()
##        elif choice == "delete":
##            delete_user()
##        elif choice == "edit":
##            edit_user()
##        elif choice == "view":
##            view_users()
##        elif choice == "block":
##            block_unblock_user()
##        elif choice == "drop":
##            drop_users()
##        elif choice == "exit":
##            break
##        else:
##            print("Invalid choice. Try again.")
##
##
### MAIN FUNCTION
##def main():
##    role, username = authenticate()
##
##    if role == "user":
##        user(username)
##    elif role == "admin":
##        admin()
##    elif role == "superadmin":
##        superadmin()
##    else:
##        print("Access Denied. Login/Registration failed.")
##
##
### INFINITE LOOP
##while True:
##    main()
##









from pymongo import MongoClient
from tabulate import tabulate

# MongoDB setup
connection = MongoClient("mongodb://localhost:27017")
print("Connected to MongoDB")
db = connection["user"]
collection = db["usermangement"]
print("Database and collection ready")

# Fix existing phone numbers
def fix_phone_format():
    for user in collection.find():
        phone = user.get("phone")
        if isinstance(phone, int) or isinstance(phone, float):
            collection.update_one(
                {"_id": user["_id"]},
                {"$set": {"phone": str(int(phone))}}
            )

fix_phone_format()

# Register a new user (default role: user)
def newuser():
    print("Register New User")
    newusername = input("Enter a new username: ")
    newpassword = input("Enter numeric password: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    age = input("Enter age: ")

    if not newpassword.isdigit():
        print("Password must contain only numbers.")
        return None
    if not phone.isdigit():
        print("Phone number must be numeric.")
        return None
    if not age.isdigit():
        print("Age must be numeric.")
        return None

    if collection.find_one({"username": newusername}):
        print("Username already exists.")
        return None

    collection.insert_one({
        "username": newusername,
        "password": newpassword,
        "phone": str(phone),
        "email": email,
        "age": int(age),
        "role": "user",
        "is_blocked": False
    })
    print("Registration successful!")
    return "user"

# Login for existing user
def existinguser():
    print("Login Existing User")
    existingusername = input("Enter your username: ")
    existingpassword = input("Enter your password: ")

    user = collection.find_one({"username": existingusername})

    if user:
        if user.get("is_blocked", False):
            print("User is blocked. Contact admin.")
            return None, None
        if user["password"] == existingpassword:
            print("Login successful.")
            return user.get("role", "user"), user["username"]
        else:
            print("Incorrect password.")
    else:
        print("User not found.")
    return None, None

# Combined authentication handler
def authenticate():
    choice = input("Are you a new user? (yes/no): ").lower()

    if choice == "yes":
        role = newuser()
        return role, None
    elif choice == "no":
        return existinguser()
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        return None, None

# USER role actions
def user(username):
    user_doc = collection.find_one({"username": username})
    if user_doc:
        print("Welcome,", user_doc["username"])
        print("Your Details:", user_doc)
        choice = input("Do you want to update your name or password? (name/password/none): ").lower()
        if choice == "name":
            new_name = input("Enter new username: ")
            collection.update_one({"username": username}, {"$set": {"username": new_name}})
            print("Name updated.")
        elif choice == "password":
            new_password = input("Enter new numeric password: ")
            if new_password.isdigit():
                collection.update_one({"username": username}, {"$set": {"password": new_password}})
                print("Password updated.")
            else:
                print("Password must be numeric.")
    else:
        print("User not found.")

# Add a user
def add_user():
    print("Add New User")
    newusername = input("Enter new username: ")
    newpassword = input("Enter numeric password: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    age = input("Enter age: ")
    role = input("Enter role (user/admin/superadmin): ").lower()

    if not newpassword.isdigit():
        print("Password must contain only numbers.")
        return
    if not phone.isdigit():
        print("Phone must be numeric.")
        return
    if not age.isdigit():
        print("Age must be numeric.")
        return
    if collection.find_one({"username": newusername}):
        print("Username already exists.")
        return

    collection.insert_one({
        "username": newusername,
        "password": newpassword,
        "phone": str(phone),
        "email": email,
        "age": int(age),
        "role": role,
        "is_blocked": False
    })
    print("User added successfully.")

# Delete a user
def delete_user():
    username = input("Enter username to delete: ")
    result = collection.delete_one({"username": username})
    if result.deleted_count > 0:
        print("User deleted.")
    else:
        print("User not found.")

# Edit a user's info
def edit_user():
    username = input("Enter username to edit: ")
    user_doc = collection.find_one({"username": username})
    if not user_doc:
        print("User not found.")
        return

    new_username = input("Enter new username (leave blank to skip): ")
    new_password = input("Enter new password (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")
    new_email = input("Enter new email (leave blank to skip): ")
    new_age = input("Enter new age (leave blank to skip): ")

    update_fields = {}
    if new_username:
        update_fields["username"] = new_username
    if new_password:
        if new_password.isdigit():
            update_fields["password"] = new_password
        else:
            print("Password must be numeric.")
            return
    if new_phone:
        if new_phone.isdigit():
            update_fields["phone"] = str(new_phone)
        else:
            print("Phone must be numeric.")
            return
    if new_email:
        update_fields["email"] = new_email
    if new_age:
        if new_age.isdigit():
            update_fields["age"] = int(new_age)
        else:
            print("Age must be numeric.")
            return

    if update_fields:
        collection.update_one({"username": username}, {"$set": update_fields})
        print("User updated successfully.")
    else:
        print("Nothing to update.")

# Block or unblock
def block_unblock_user():
    username = input("Enter username to block/unblock: ")
    user_doc = collection.find_one({"username": username})
    if user_doc:
        current_status = user_doc.get("is_blocked", False)
        new_status = not current_status
        collection.update_one({"username": username}, {"$set": {"is_blocked": new_status}})
        print(f"User {'blocked' if new_status else 'unblocked'} successfully.")
    else:
        print("User not found.")

# View users in tabular format
def view_users(filter_out=None):
    print("\nAll Users:")
    headers = ["Username", "Phone", "Email", "Age", "Role", "Blocked"]
    table = []
    for doc in collection.find():
        if filter_out and doc.get("role") == filter_out:
            continue
        table.append([
            doc.get("username"),
            doc.get("phone"),
            doc.get("email"),
            doc.get("age"),
            doc.get("role"),
            doc.get("is_blocked", False)
        ])
    print(tabulate(table, headers=headers, tablefmt="grid"))

# Drop the entire collection
def drop_users():
    confirm = input("Are you sure you want to drop the collection? (yes/no): ").lower()
    if confirm == "yes":
        collection.drop()
        print("Collection dropped.")
    else:
        print("Collection not dropped.")

# Admin menu
def admin():
    print("Welcome Admin!")
    while True:
        choice = input("Choose operation (add/delete/edit/view/exit): ").lower()
        if choice == "add":
            add_user()
        elif choice == "delete":
            delete_user()
        elif choice == "edit":
            edit_user()
        elif choice == "view":
            view_users(filter_out="superadmin")
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Try again.")

# Superadmin menu
def superadmin():
    print("Welcome Superadmin!")
    while True:
        choice = input("Choose operation (add/delete/edit/view/block/drop/exit): ").lower()
        if choice == "add":
            add_user()
        elif choice == "delete":
            delete_user()
        elif choice == "edit":
            edit_user()
        elif choice == "view":
            view_users()
        elif choice == "block":
            block_unblock_user()
        elif choice == "drop":
            drop_users()
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Try again.")

# Main function
def main():
    role, username = authenticate()

    if role == "user":
        user(username)
    elif role == "admin":
        admin()
    elif role == "superadmin":
        superadmin()
    else:
        print("Access Denied. Login/Registration failed.")

# Run loop
while True:
    main()

