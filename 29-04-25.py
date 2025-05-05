##def ispalindrome(string):
##    word=string.lower()
##    return word==word[::-1]
##print(ispalindrome("madam"))
##print(ispalindrome("hello"))
##
##
##def calculator(a,b,operation):
##    if operation=="add":
##        return a+b
##    elif operation=="sub":
##        return a-b
##    elif operation=="mul":
##        return a*b
##    elif operation=="div":
##        return a/b
##    else:
##        return "invalid syntax"
##     
##print(calculator(10,5,"add"))
##print(calculator(10,5,"sub"))
##print(calculator(10,5,"mul"))
##print(calculator(10,5,"div"))
##
##
##def count_vowels(string):
##    string = string.lower()
##    count = 0
##    for char in string:
##        if char in "aeiou":
##            count += 1
##    print(count)
##
##count_vowels("qwerttdiweugfjsh")

##
##def multiply_num(*arg):
##    mul=1
##    for i in arg:
##        print(i)
##        mul*=i
##        print(mul)
##        
##print(multiply_num(2,3,4))
##print(multiply_num(5,10))



##def sum_average(*num):
##    add=sum(num)
##    average=sum(num)/len(num)
##    return add,average
##print(sum_average(10,20,30))
##print(sum_average(5,15))

count = 0  

def say_hello():
    global count
    count += 1
    print(count)


say_hello()

say_hello()  
say_hello()  
say_hello()  
print(say_hello())
    
