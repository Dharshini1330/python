##from  pymongo import MongoClient
##client = MongoClient("mongodb://localhost:27017/")
##db = client["minitask"]
##collection = db["library management"]
####print("connection established")
##collection.insert_one("list_books")
##if collection.count_documents({}) == 0:
##    collection.insert_many(list_books)
##    print("Data inserted into MongoDB.")
##else:
##    print("️ MongoDB already contains data. Skipping insertion.")

##print(" Welcome to Library Management System")

print("welcome to library management")

##user=input("how may i help you?").lower()
##error fixtion in 1 when space is made
list_books = [
    {
        "fiction": [
            "One Hu+ndred Years of Solitude", "Crime and Punishment", "The Kite Runner", "Life of Pi",
            "The Shining", "The Girl on the Train", "Little Women", "The Da Vinci Code",
            "A Tale of Two Cities", "Wuthering Heights", "Gone Girl", "Me Before You",
            "A Thousand Splendid Suns", "The Time Traveler’s Wife", "The Secret Garden",
            "The Midnight Library", "Where the Crawdads Sing", "The Night Circus",
            "The Shadow of the Wind", "The Silent Patient"
        ]
    },
    {
        "science fiction": [
            "Dune", "Ready Player One", "Ender's Game", "The Name of the Wind",
            "Mistborn: The Final Empire", "The Hunger Games", "Divergent", "Eragon",
            "The Maze Runner", "A Game of Thrones", "The Wheel of Time", "An Ember in the Ashes",
            "Red Queen", "Legend", "Artemis", "The Left Hand of Darkness", "Neuromancer",
            "The Martian", "Shadow and Bone", "Children of Blood and Bone"
        ]
    },
    {
        "biography": [
            "Becoming", "Steve Jobs", "Educated", "I Am Malala", "Long Walk to Freedom",
            "The Diary of a Young Girl", "Shoe Dog", "Elon Musk", "The Story of My Experiments with Truth",
            "When Breath Becomes Air", "Born a Crime", "The Glass Castle", "Eat Pray Love",
            "Wild", "The Wright Brothers", "Alexander Hamilton", "Open", "My Life in Full",
            "Unbroken", "A Life on Our Planet"
        ]
    },
    {
        "self help": [
            "Atomic Habits", "The Power of Now", "Think and Grow Rich", 
            "How to Win Friends and Influence People", "Deep Work", 
            "The 7 Habits of Highly Effective People", "Grit", "Can’t Hurt Me",
            "The Subtle Art of Not Giving a F*ck", "Rich Dad Poor Dad",
            "You Are a Badass", "Ikigai", "The Four Agreements", "Make Your Bed",
            "Think Like a Monk", "Mindset", "Start with Why", "Essentialism",
            "The Miracle Morning", "Tools of Titans"
        ]
    },
    {
        "technology / programming": [
            "Python Crash Course", "Automate the Boring Stuff with Python", "Clean Code",
            "The Pragmatic Programmer", "Introduction to Algorithms", 
            "Hands-On Machine Learning with Scikit-Learn", "Fluent Python",
            "Data Structures and Algorithms in Python", "Grokking Algorithms",
            "Effective Python", "JavaScript: The Good Parts", "Head First Java",
            "Eloquent JavaScript", "Learning Python", "Design Patterns",
            "Artificial Intelligence: A Modern Approach", "You Don't Know JS",
            "Programming Pearls", "C Programming Language", "Code Complete"
        ]
    },
    {
        "spiritual / motivational": [
            "The Monk Who Sold His Ferrari", "Tuesdays with Morrie", "The Bhagavad Gita",
            "The Art of Happiness", "Who Will Cry When You Die?", "The Prophet", 
            "The Power of Positive Thinking", "Think Like a Monk", "Awaken the Giant Within",
            "The Magic of Thinking Big", "The Book of Joy", "Your Soul’s Plan", 
            "The Way of the Superior Man", "The Untethered Soul", "The Secret",
            "The Seven Spiritual Laws of Success", "Conversations with God",
            "Man’s Search for Meaning", "The Road Less Traveled", "As a Man Thinketh"
        ]
    }
]

# ####to add a book
# ##if user == add a book:
# ##    book=input("enter book name")
# ##    if book != list_books:
# ##        list_books.append(book)
# ##        print(list_books)
# ##    else:
# ##        print("the book already exists")
# ##
# ####to remove a book
# ##    
# ##elif user == remove a book:
# ##    books= input("enter book name")
# ##    list_books.remove(books)
# ##    print(list_books)






# print("Welcome to Library Management")
# user = input("How may I help you? ").lower()

# # Checking for 'add a book'
# if user == "add a book":
#     genre = input("Enter genre to add book under: ")
#     book = input("Enter book name: ")

#     found = False
#     for category in list_books:
#         if genre in category:
#             if book not in category[genre]:
#                 category[genre].append(book)
#                 print(f"'{book}' added successfully under '{genre}'.")
#             else:
#                 print("The book already exists in that genre.")
#             found = True
#             break
#     if not found:
#         print("Genre not found!")

# # Checking for 'remove a book'
# elif user == "remove a book":
#     genre = input("Enter genre of the book: ")
#     book = input("Enter book name to remove: ")

#     found = False
#     for category in list_books:
#         if genre in category:
#             if book in category[genre]:
#                 category[genre].remove(book)
#                 print(f"'{book}' removed from '{genre}'.")
#             else:
#                 print("Book not found in that genre.")
#             found = True
#             break
#     if not found:
#         print("Genre not found!")

# else:
#     print("Invalid option. Please type 'add a book' or 'remove a book'.")

# Start the loop
while True:
    print("\n------ MENU ------")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. View all books by genre")
    print("4. Search for a book")
    print("5. Add a new genre")
    print("6. List all genres")
    print("7. Exit")

    user = input("\nChoose an option (1-7): ").strip().lower()

    # Exit condition
    if user == "7" or user == "exit":
        print(" Thank you for using the Library System!")
        break

    # Add a Book
    elif user == "1" or user == "add a book":
        genre = input("Enter the genre to add the book under: ").strip().lower()
        book = input("Enter the book name to add: ").strip().title()

        found = False
        for category in list_books:
            if genre in category:
                if book not in category[genre]:
                    category[genre].append(book)
                    print(f" '{book}' has been added to '{genre}'.")
                else:
                    print(f"The book '{book}' already exists in '{genre}'.")
                found = True
                break
        if not found:
            print(f" Genre '{genre}' not found. Please add it first using option 5.")

    # Remove a Book
    elif user == "2" or user == "remove a book":
        genre = input("Enter the genre of the book: ").strip().lower()
        book = input("Enter the book name to remove: ").strip().title()

        found = False
        for category in list_books:
            if genre in category:
                if book in category[genre]:
                    category[genre].remove(book)
                    print(f"'{book}' removed from '{genre}'.")
                else:
                    print(f"Book '{book}' not found in genre '{genre}'.")
                found = True
                break
        if not found:
            print(f" Genre '{genre}' not found.")

    # View All Books
    elif user == "3" or user == "view books":
        print("\n Library Books by Genre:")
        for category in list_books:
            for genre, books in category.items():
                print(f"\n🔸 {genre}:")
                for book in books:
                    print(f"   - {book}")

    # Search for a Book
    elif user == "4" or user == "search book":
        book_name = input("Enter the book name to search: ").strip().title()
        found = False
        for category in list_books:
            for genre, books in category.items():
                if book_name in books:
                    print(f" '{book_name}' is available in '{genre}' genre.")
                    found = True
        if not found:
            print(f" Book '{book_name}' not found in any genre.")

    # Add New Genre
    elif user == "5" or user == "add genre":
        new_genre = input("Enter the new genre name: ").strip()
        exists = any(new_genre in genre_dict for genre_dict in list_books)
        if not exists:
            list_books.append({new_genre: []})
            print(f" New genre '{new_genre}' added successfully.")
        else:
            print("️ Genre already exists.")

    # List All Genres
    elif user == "6" or user == "list genres":
        print("\n Available Genres:")
        for category in list_books:
            for genre in category:
                print(f" - {genre}")

    else:
        print("️ Invalid option. Please enter a number between 1 to 7.")    
