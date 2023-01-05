# import datetime
# import time
# today = datetime.datetime.now()
# today = datetime.date.today()
# print(today)

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime('%A'))

# x = datetime.datetime.now()
# print(x.month)

# x = datetime.datetime.now()
# print(x.day)

# x = datetime.datetime.now()
# print(x.hour)

# x = datetime.datetime.now()
# print(x.minute)

# x = datetime.datetime.now()
# print(x.second)

# Time = datetime.time(11, 34, 56)
# print("hour =", Time.hour)
# print("minute =", Time.minute)
# print("second =", Time.second)
# print("microsecond =", Time.microsecond)

# x = time.time()
# print(x)

# localtime = time.time()       # Return Seconds
# localtime = time.localtime(time.time())   # Returns Time Structure
# localtime = time.asctime(time.localtime(time.time()))  # Returns time in presentable format
# print(localtime)


# today = datetime.datetime.now()
# print(today)

# yesterday = today - datetime.timedelta(days=1)
# print(yesterday)

# tomorrow = today + datetime.timedelta(days=1)
# print(tomorrow)

# initial = time.time()
# for i in range(1,21):
#     time.sleep(.5)
#     print(i,end=" ")
# print("For loop takes:",time.time()-initial)
# print()

# initial2 = time.time()
# t = 1
# while(t<=20):
#     time.sleep(.5)
#     print(t,end=" ")
#     t+=1
# print("While loop takes:",time.time()-initial2)
