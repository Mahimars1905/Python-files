# Control Statement in Python
# For Loop While Loop

# Print counting 1 to 10
# for i in range(11):
#     print(i,end=" ")

# i = 1
# while(i<=10):
#     print(i)
#     i=i+1

# Sum of n natural numbers
# 1 + 2 + 3 + 4-------- 55

# num = int(input("Enter Number: "))
# sum = 0
# for i in range(1,num+1):
#     sum = sum + i
# print(f"The sum from 1 to {num} is: ", sum)

# Print a factorial of a number
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
# print(f"The factorial of {num} is: ", fact)

# WAP to print reverse of a number  (123 - 321)
# WAP to count digits in a number (123 - 3)
# WAP to check a number is armstrong number (153 = 1+125+27)
# WAP to check a number is perfect number (28 = 1+2+4+7+14)
# WAP to check a number is strong number (145 = 1+24+120)
# WAP to check a number is palindrome number (121 = 121)


# 1 - #  check reverse of a number
# num=int(input("Enter a number: "))
# rev=0
# while(num!=0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

# 2 - Factorial
# num=int(input("Enter a number: "))
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
# print(fact)

# num=int(input("Enter a number: "))
# i = 1
# fact = 1
# while(i<=num):
#     fact = fact * i
#     i = i+1
# print(fact)
    

# 2 - # Strong  Number
# num=int(input("Enter a number: "))
# sum=0
# temp=num 
# while(num):
#     i=1
#     fact=1
#     rem=num%10
#     while(i<=rem):
#         fact=fact*i
#         i=i+1
#     sum=sum+fact
#     num=num//10
# if(sum==temp):
#     print("Strong Number")
# else:
#     print("Not a Strong number")

#  3 - # Palindrome Number
# num=int(input("Enter a number: "))
# temp=num
# rev=0
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# if(temp==rev):
#     print("This is a Palindrome number")
# else:
#     print("Not a Palindrome number")

# 4 - Armstrong number
# num=int(input("Enter a number: "))
# sum=0
# temp=num
# while(temp>0):
#     digit=temp%10
#     sum=digit**3 + sum
#     temp = temp//10
    
# if (num==sum):
#     print("num is a armstrong number")
# else:
#     print("num is not a armstrong number")

# 5 - Count Digits
# num=int(input("Enter number: "))
# count=0
# temp = num
# while(temp>0):
#     digit = temp%10
#     # count = count + 1
#     temp = temp//10
#     count = count + 1
# print(count)

# 6- Check perfect number
# num=int(input("Enter number: "))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if sum==num:
#     print("Perfect Number")
# else:
#     print("Not a perfect number")
    
    

    



