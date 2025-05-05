# 1. Default and Keyword Arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                
greet(name="Bob", greeting="Hi")  



# 2. Arbitrary Positional Arguments (*args)
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(2, 3, 4))  


# 3. Arbitrary Keyword Arguments (**kwargs)
def print_user_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_details(name="John", age=30, location="New York")


# 4. Recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))  


# 5. Lambda with filter()
nums = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = list(filter(lambda x: x % 2 != 0, nums))
print(odd_numbers)  


# 6. Function Returning a Function (Closure)
def power_raiser(n):
    return lambda x: x ** n

square = power_raiser(2)
print(square(5))  


# 7. Function with Type Hinting
def concatenate_strings(a: str, b: str) -> str:
    return a + b

print(concatenate_strings("Hello, ", "world!"))

# 8. Pass Function as Argument
def operate(a, b, func):
    return func(a, b)

def add(x, y):
    return x + y

print(operate(2, 3, add))  


# 9. Nested Functions
def outer():
    def inner():
        print("Inner function called")
    inner()

outer()


# 10. Memoization with Dictionary
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(10))  
