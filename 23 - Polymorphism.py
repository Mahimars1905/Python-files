# Polymorphism means same function with different signatures/parameters
# There are 2 types of polymorphism
# 1 - Run Time (Method Overriding)
# 2 - Compile Time (Method Overloading)


# def add(x,y=0,z=0):
#     print(x+y+z)
# add(2)
# add(2,3)
# add(2,3,4)

# Polymorphism with class method
class Programmer:
    def work(self):
        print("I am a Python Programmer")
class Developer:
    def work(self):
        print("I am a Java Developer")
        
pro = Programmer()
dev = Developer()
pro.work()
dev.work()