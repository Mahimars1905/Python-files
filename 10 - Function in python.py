# Function = Function is a block of code. We can call functions in our programs according to our need. 
# def hello():     # creating a function
#     print("Good Morning")
# hello()

# def myfunc(name):        # Function with parameter
#     print("My name is: ", name)
# myfunc("Mahima")
# myfunc("Radha")
# myfunc("Nipun")
# myfunc("Amit")
# myfunc("Suresh")

# def myfunc(fname, lname):        # Function with parameter
#     print("My name is: ", fname, lname)
# myfunc("Mahima", "Singh")
# myfunc("Radha", "Singh")
# myfunc("Nipun","Singh")
# myfunc("Amit","Singh")
# myfunc("Suresh","Singh")


# def myfunc(fname, lname="Singh"):        # Function with default parameter
#     print("My name is: ", fname, lname)
# myfunc("Mahima")
# myfunc("Radha")
# myfunc("Nipun")
# myfunc("Amit")
# myfunc("Suresh")


# def addition(a, b):
    # print(a + b)
# addition(20,40)

# a = 20
# if(a%2==0):
    # print("Even Number")
    # 
# def oddeven(a):
    # if(a%2==0):
        # print("Even Number")
# oddeven(10)

# 1 Calculator
# def calculator(a,b):
#     print(f"Addition of {a} and {b} is: ", a+b )
#     print(f"Substraction of {a} and {b} is: ",a-b)
#     print(f"Division of {a} and {b}  is: ",a/b)
#     print(f"Multiplication of {a} and {b} is: ",a*b)
# calculator(20,4)
# calculator(40,5)

# 2 Even or Odd
# def even_or_odd(a):
#     if(a%2==0):
#         print("Number is even")
#     else:
#         print("Number is odd")
# even_or_odd(20)

# 3 Greater value
# def greater(a,b,c):
#     if(a>b and a>c):
#         print("A is greater")
#     elif(b>a and b>c):
#         print("B is greater")
#     else:
#         print("C is greater")
# greater(24,87,45)

# 4 check a year is Leap year or normal year
# def leapyear():
#     a=int(input("Enter year: "))
#     if(a%4==0 and a%100!=0)or (a%400==0):
#         print("This year is leap year!")
#     else:
#         print("This year is not a leap year!")
#  leapyear()

# 5  Count Digits
# def countdigit():
#     num=int(input("Enter number: "))
#     count=0
#     temp=num
#     while(temp>0):
#         digit=temp%10
#         temp=temp//10
#         count=count+1
#     print(count)
# countdigit()


# import file name           # for call multipal functions from other file

# import functions          
# functions.greater(34,345,3421)
# functions.even_or_odd(78)

# from file name import function name    # for  call one function from other file

# from functions import even_or_odd   
# even_or_odd(53)

# from functions import greater
# greater(54,55,45)