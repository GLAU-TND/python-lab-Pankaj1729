try:
    a=int(input())
    b=int(input())
    c=input()
    s=a+b
    p=a+c#Type Error
    a.append(c)#attribute Error

except ValueError:
    raise ValueError("Value Error Occured")
except TypeError:
    raise TypeError("Type Error Occured")
except AttributeError:
    raise AttributeError("Attribute Error Occured")
