# # 1- check number is "even" or "odd"
# a=int(input("Enter a number: "))
# if(a%2==0):
#     print("Number is even ")
# else:
#     print("Number is odd ")

# # 2- check number is divisibal by 4 and 6 or not
# a=int(input("Enter a number: "))
# if(a%4==0 and a%6==0):
#     print(" This Number is divisibal by 4 and 6 ")
# else:
#     print("This Number is not divisibal by 4 and 6")

# # 3- check year is leap year or other year
# a=int(input(" Enter any year: "))
# if(a%4==0 and a%100!=0) or(a%400==0):
#     print('This year is "Leap" year')
# else:
#     print("This year is not a Leap year ")

# 3- check value is vowel or consonant
# str=(input("Enter any String: "))
# if(str=="a" or str=="e" or str=="i" or str=="o" or str=="u" or str=="A" or str=="E" or str=="I" or str=="O" or str=="U"):
#     print(" This is a Vowel ")
# else:
#     print("This is a Consonant")
    
# # 4- check number is negative, posotive or zero
# a=int(input("Enter any number: "))
# if(a>0):
#     print("Number is positive: ")
# elif(a<0):
#     print("Number is negative")
# else:
#     print("Number is zero")

# # 5-check alphabet is lower case or upper case
# var=(input("Enter any string: "))
# 
    
# sum of even number
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# sum = 0
# for i in range(a, b+1):
#     if(i%2==0):
#         print(i, end=" ")
#         sum = sum + i
# print()
# print("Sum of {a} to {b} even numbers: ", sum)


class Programmer:
    def__init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def prodetailes(self):
    print(f"The name is {self.name}, age is{self.age} and salary is {self.salary}") 
    
class Developer:
    def__init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def devdetailes(self):
        print(f"The name is {self.name}, age is {self.age} and salary is {self. salary}")


        
