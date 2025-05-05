###task1
##num=[1,2,3,4,5,6,7,8,9,10]
##print(num)
###task2
##num=[1,2,3,4,5,6,7,8,9,10]
##print(num[0])
##print(num[-1])
###task3
##um=[1,2,3,4,5,6,7,8,9,10]
##num.append(11)
##print(num)
###task4
##num=[1,2,3,4,5,6,7,8,9,10]
##num.insert(2,0)
##print(num)
###task5
##num=[1,2,3,4,5,6,7,8,9,10]
##num.remove(2)#value
##num.pop(3)#index
##print(num)
#task6
num=[1,2,3,4,5,6,7,8,9,10]
for i in range(-1,-(len(num)+1),-1):
     print(num[i])
#task7
##num=[1,122,30,54,504,64,709,87,99,10]
##num.sort()
##number=[1,122,30,54,504,64,709,87,99,10]
##number.sort(reverse=True)
##print(num)
##print(number)
###task8
##number=[1,122,30,54,504,64,709,87,99,10]
##for i in number:
##    if i%2==0:
##        print(i)
#####task9
##number=[1,122,30,54,504,64,709,87,99,10]
##total=0
##for i in number:
##    total+=i
##print(total)
###task10
##number = [1, 122, 30, 54, 504, 64, 709, 87, 99, 10]
##total = 0
##for i in number:
##    if i % 2 != 0:
##        total+=1
##
##print( total)
#task11
##num=[1,2,3,4,5]
##a=2
##for i in num:
##    y=i**a
##    print(y)
###task12
##number = [1, 122, 30, 54, 504, 64, 709, 87, 99, 10]
##maxvalue = 0 
##for i in number:
##    if i > maxvalue:
##        maxvalue = i
##print("Maximum value is", maxvalue)
##
##number = [1, 122, 30, 54, 504, 64, 709, 87, 99, 10]
##minvalue = 0  
##for i in number:
##    if i < minvalue:
##        minvalue = i
##print("Minimum value is", minvalue)
#####task13=============>>>>>>>>>>>bending
##string=["num","int","num","float","float"]
##dup=string
##print(string)
##for i in string:
##    print(i)
##    if i == string:
##        string.remove()
####        print(string)
##
###task13
##list_ = [1, 2, 2, 3, 4, 4, 5]
##dup_list = list(set(list_))
##print( dup_list)
###task14
##list1 = [1, 2, 3]
##list2 = [3, 4, 5]
##merged_unique = list(set(list1 + list2))
##print( merged_unique)
###task15
##list1 = [1, 2, 3]
##list2 = [4, 5, 3]
##list3 = (set(list1) & set(list2))
##print(list3)
###task16
##list_num=[10,200,4653,474,53578]
##list_num.sort()
##print(list_num[-2])
###task17
##my_list = [1, 2, 3, 4, 5]
##rotated = my_list[2:] + my_list[:2]
##print( rotated)
###task18
##words = ["madam", "python", "radar"]
##for word in words:
##    if word == word[::-1]:
##     print(word)
##
#####task19
##result=[f"{i}" if i%2==0 else "odd" for i in range(50)]
##print(result)
###task20
##string=["blue","grey","black","gold","voilet","tulip","rose"]
##res=[len(i) for i in string]
##print(res)
##result=[len(i) for i in ["blue","grey","black","gold","voilet","tulip","rose"]]
##print(result)
###task21
##result=[f"{-i}" for i in range(-1,-50,-1)]
##print(result)
######################################################################################################
####task1
num=int(input("enter a number:"))
for i in range(1,num+1):
    if i%2==0:
        print(i,"it is a even number")
    else:
        print(i,"it is a odd number")
####task2=>greatest number 
##num1=int(input("enter the first number:"))
##num2=int(input("enter the second number:"))
##num3=int(input("enter the third number:"))
##for i in range
##task3=> smallest number
        
##task4
num=int(input("enter a number:"))
for i in range(1,num+1):
    if i>0:
        print(i,"is a positive number")
    elif i<0:
        print(i," is a negative number")
    else:
        print(i)

##task5
num=int(input("enter a number:"))
count=0
for i in range(num+1):
    count+=i
print(count)
##task6
                                                
