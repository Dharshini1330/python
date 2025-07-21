##a=2
##b=4
##a,b=b,a
##print(a)
##print(b)
##print("////////////////////////")
##n=int(input("enter a number"))
##list1=[]
##for val in range(0,n,1):
##    ele=int(input("enter a number"))
##    list1.append(ele)
##    print(list1)
##for val in range(0,n,1):
##    ele=list1.pop(0)
##    list1.append(ele)
##    print(list1)
##print("////////////////////////")
##import math
##x1=int(input("enter a number"))
##x2=int(input("enter a number"))
##y1=int(input("enter a number"))
##y2=int(input("enter a number"))
##dx=x2-x1
##dy=y2-y1
##d=dx**2+dy**2
##print(math.sqrt(d))
##print("////////////////////////")
##n=int(input("enter a number"))
##i=1
##x=0
##while i<=n:
##    x=x*2+1
##    print(x,sep="")
##    i+=1
print("////////////////////////")
n=int(input("enter a number"))
for i in range(1, n + 1):
    for j in range(i):
        print(i,end="")
    print()
##print("////////////////////////")
n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print("")
##print("////////////////////////")
##n = int(input("Enter a number: "))
##for i in range(1, n + 1):
##    for j in range(i):
##        print(i, end="")  # Stay on the same line
##    print()  # Move to next line after inner loop
##
##
