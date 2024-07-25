'''''''''
def divide(x,y):
    try:
        resulr=x/y
        print(resulr)
    except ZeroDivisionError as e:
        print("cannot divide by zero")
        print("error:",e)
       
    finally:
        print("execution completed")

print(divide(20,5))  
print(divide(3,0))     
'''''''''


