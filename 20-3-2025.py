###task1
num=int(input("enter the number"))
if(num>0):
    print("it is a positive number")
else:
    print("it is a negative number")
###task2
num=int(input("enter the number"))
if(num % 2 == 0):
    print("it is a even number")
else:
    print("it is an odd number")
###task3
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a > b and a > c:
    print(f"The greatest number is",a)
elif b > a and b > c:
    print(f"The greatest number is ",b)
else:
    print(f"The greatest number is ",c)
###task4
num=int(input("enter the number"))
if(num % 3 == 0 and num % 11 == 0):
    print("it is divisible by 3 and 11 ")
else:
    print("it is not divisible")
###task5
num=int(input("enter your marks"))
if(num >= 90):
    print("your grade is A++")
elif(num>=75):
     print("your grade is B++")
elif(num>=50):
    print("your grade is C++")
elif(num>=30):
    print("your grade is D++")
else:
    print("you failed")
###task6
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year ,"is not a leap year")
#task7
age=int(input("enter your age"))
if(age >= 18):
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")
#task8
age=int(input("enter your age"))
income=int(input("enter your income"))
if(age >= 21) and (income >= 300000):
    print("you are eligible for loan")
else:
     print("you are not eligible for loan")
#task9
unit=int(input("enter your unit"))
if(unit <= 100):
         print("enter your unit is",unit*5)
elif(unit <= 300):
         print("enter your unit is",unit*7)
else:
         print("enter your unit is",unit*10)
#task10
num=int(input("enter your number"))
if(num % 3):
         print("FIZZ")
elif(num % 3==0 )and (num % 5==0):
         print("FIZZBUZZ")
elif(num % 5):
         print("BUZZ")
else:
    print("error")
#task11
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))


if a == b == c:
    print("It is an Equilateral Triangle")
elif a == b or b == c or a == c:
    print("It is an Isosceles Triangle")
else:
    print("It is a Scalene Triangle")



    




         


