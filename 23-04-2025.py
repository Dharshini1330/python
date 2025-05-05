#task1
my_dict={}
print(my_dict)
my_dict.update(name="alice",age=25,city="new york")
print(my_dict)
#task2
my_dict["email"]="alice@gmail.com"
my_dict["phone"]=123-456-789
print(my_dict)
#task3
my_dict.update(age=26,city="los angeles")
print(my_dict)
#task4
del my_dict["phone"]
print(my_dict)
#task5
my_dict.pop("email")
print(my_dict)
#task6
my_dict["name"]="alicesmith"
print(my_dict)
#task7
my_dict.update(age=27,city="USAS")
print(my_dict)
#task8
my_dict.clear()
print(my_dict)
