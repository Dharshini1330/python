fruits={"apple":100,"banana":200,"cherry":300,"dragon fruit":400,"elderberry":500}
##task1
print(fruits)
##task2
print(fruits["apple"])
##task3
fruits.update({"apple": 650})
print(fruits)
##task4
fruits.update({"strawberry": 150})
print(fruits)
##task5
fruits.pop("strawberry")
print(fruits)
##task6
if "apple" in fruits:
    print("yes it is in")
##task7
for i in fruits:
    print(i)
##task8
for i in fruits.values():
    print(i)
##task9
for key, value in fruits.items():
    print(key,value)
##task10
print(len(fruits))
##task11
for i in fruits.items():
    print(fruits)
##task12
    student = {
    "name": "Alice",
    "age": 20,
    "subjects": {
        "math": 90,
        "science": 85,
        "english": 88
    }
}
print(student)
##task13
squares = {x: x**2 for x in range(1, 11)}
print(squares)
##task=> not done
##task15
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Using update
merged = dict1.copy()
merged.update(dict2)
print(merged)
# Using |
merged2 = dict1 | dict2
print(merged2)

##task16
if fruits.get("watermelon")in fruits:
    print("yes it is in" )
else:
    print("no it is not")

