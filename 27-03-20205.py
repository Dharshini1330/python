#question1=>even
n = int(input("Enter a number: "))
for i in range(n):
    if i % 2 == 0:
        print(i)
   
#question2=>odd
n = int(input("Enter a number: "))
for i in range(n):
    if i % 2 != 0: 
        print(i)
#question3
n=int(input("enter a number"))
for i in range(1,n+1):
      print("*"*i)
#question4
n=int(input("enter a number"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)
###question5
n=int(input("enter a number"))
for i in range(1,11):
    print(n,"x",i,"=",i)
