#q1
num=(input("enter a num"))
add=0
for i in num:
    add += int(i)
print(add)
#q2
num=(input("enter a num"))
reverse=0
for i in range(len(num)):
    temp=int(num%10)
    reverse=(reverse*10)+temp
    num=int(num//10)
print(i)
