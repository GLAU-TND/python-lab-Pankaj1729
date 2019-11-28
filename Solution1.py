class MyException(Exception):
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return str(self.x)

def Xyz(a,b):
        if a+b<150:
            raise MyException("Custom Exception Occurred")
        else:
            return a+b
a=int(input())
b=int(input())
print(Xyz(a,b))
