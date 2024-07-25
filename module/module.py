def add(a,b):
    return a+b

def sub(a,b):
    return a-b

class Calculator:
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            raise ValueError("cannot divide vy zero")
        return a/b