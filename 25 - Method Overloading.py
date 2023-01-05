class Calc:
    def func(self, x=None, y=None):
        if x==None and y==None:
            print("Hello! Good Moring")
        elif x!=None and y==None:
            fact = 1
            for i in range(1,x+1):
                fact = fact * i
            print("Factorial is:",fact)
        else:
            print("Addition is:",x+y)
obj = Calc()
obj.func(5)