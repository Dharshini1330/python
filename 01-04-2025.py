string=input("enter a word")
vowel="aeiou"
result=0
for i in string :
    if i in vowel:
        result +=1
print(result)
result=0
a=int(input("enter a num"))
for i in a:
    result+=int(i)**len(a)
print(result)
num=int(input("enter a num"))
a,b=0,1
print(a,b)
for i in range(num):
     c=a+b
     a=b
     b=c
     print(c)
