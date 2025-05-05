fruits={"apple","banana","cherry","orange","starwberry","kiwi"}
#task1
print(fruits)
#task2
fruits.add("blueberry")
print(fruits)
#task3
fruits.remove("banana")
print(fruits)
#task4
fruits.discard("cherry")
print(fruits)
#task5
if "apple" in fruits:
    print("apple is in the list")
#task6
fruits={"apple","apple","banana","cherry","orange","starwberry","kiwi"}
print(fruits)
#task10
fruits.clear()
print(fruits)
set_1={1,2,3}
set_2={3,4,5}
#task7
set3=set_1|set_2
print(set3)
#task8
set3=set_1&set_2
print(set3)
#task9
set3=set_1-set_2
print(set3)
#task11
set_1={1,2,3}
set_2={3,4,5,3,2,1}
set_3 = set_1.issubset(set_2)
print(set_3)
#task12
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list = list(set(my_list))
print(my_list)
#task13
list_1 = [1,2,3,4,5]
list_2 = [6,1,7,8,9,10]
list_3=set(list_1)&set(list_2)
print(list_3)
#task14
text = "hello world"
unique_chars = set(text)
print( unique_chars)
print( len(unique_chars))

#task15
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3= set1.isdisjoint(set2)
print(set3)

#task16
student_names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]
unique_names = set(student_names)
print( unique_names)






