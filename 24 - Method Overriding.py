class A:
    def func(self):
        print("Good Morning")
class B(A):
    def func(self):
        print("Good Evening")
        
    def wish(self):
        print("Good Night")
        
ob = A()
ob.func()