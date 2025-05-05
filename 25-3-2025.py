#question 1
num=int(input("give  a number"))
if(num % 3 == 0):
   print("it is divisible by 3")
else:
   print("it is not divisible by three")

#question 4
name=input("enter your name")
dupname="buzz"
if(name==dupname):
    print(" buzz have a happy day")
    
#question8
alphabet=input("enter a letter")
if(alphabet in "a,e,i,o,u"):
    print("it is a vowel")
else:
 print("false")
#question 9
num=int(input("give  a number"))
if(num > 18):
    print("old enough")
else:
    print("too young")
#question 10
password=(input(""))
duppassword=1234
if (password == ""):
    print("please!enter your password")
elif( int(password)==duppassword):
    print("correct!the password you entered matches the original password")
else:
   print("incorrect password")
#question11
age = int(input("Enter your age: "))
originalprice = 100000  

if age <= 10:
    print("Free cost")
elif age >= 70:  
    finalprice = originalprice - (originalprice * 40 / 100)  
    print("Final price is", finalprice)
elif age >= 35:
    finalprice = originalprice - (originalprice * 50 / 100)
    print("Final price is", finalprice)
else:
    finalprice = originalprice - (originalprice * 70 / 100)
    print("Final price is", finalprice)


