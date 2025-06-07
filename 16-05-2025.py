##task1

##try:
##    num1=int(input("enter a num1"))
##    num2=int(input("enter a num2"))
##    result=num1/num2
##    print("result:",result)
##except ZeroDivisionError:
##    print("oops you entered zero which is not possible")
##finally:
##    print("task completed")
## task2
##try:
##    age = int(input("Enter your age: "))
##    
##    if age <= 0:
##        raise ValueError("Enter a valid age")
##
##    if age >= 18:
##        print("You are eligible for voting")
##    else:
##        print("You are not eligible for voting")
##
##except ValueError as e:
##    print("Error:", e)
##
##finally:
##    print("Task done")
##task3
##my_list = [10, 20, 30, 40, 50]
##
##try:
##    index = int(input("Enter an index (0 to 4): "))
##    print(f"Element at index {index}: {my_list[index]}")
##except IndexError:
##    print("Error: Index out of range. Please enter a value between 0 and 4.")
##except ValueError:
##    print("Error: Please enter a valid integer.")
##finally:
##    print("Task completed.")
##task5
##
##try:
##    num1=input("enter a num")
##    num2=int(input("enter a num"))
##    res=num1+num2
##    print(result)
##except TypeError:
##    print("operation is not successfull because one is intger and the other is string")
##except Exception as e:
##    print(e)
##finally:
##    print("done")
##task6
##try:
##    num=int(input("enter a number"))
##    result=100/num
##    print("result:",result)
##except  ValueError:
##    print("enter a valid value")
##except ZeroDivisionError:
##    print("enter a valid number without zero")
##finally:
##    print("task completed")
##task7
##try:
##    num1=int(input("enter a number_1"))
##    num2=int(input("enter a number_2"))
##    div=num1/num2
##    
##except ZeroDivisionError:
##    print("operation can't be done because it has zero")
##else:
##    print("the result is:",div )
##finally:
##    print("the task has done successfully")
## task8
##try:
##    num1=int(input("enter a num_1"))
##    num2=int(input("enter a num_2"))
##    div=num1/num2
##    print("result",div)
##except ZeroDivisionError:
##    print("oops you entered zero")
##except ValueError:
##    print("enter a correct value")
##finally:
##    print("mission succesfully")


##task10
##def List(no,index):
##        return no[index]
##try:
##    res=int(input("enter a index number from 0 to 4"))
##    mylist=[10,20,30,40,50]
##    print(List(mylist,res))
##    
##except IndexError:
##    print("you have entered a wrong index number")
##except ValueError:
##    print("enter the correct value")
##finally:
##    print("execution done successfully")






         
