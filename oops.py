# class classname:
#     def print():
#         print("my name is prabesh")
# obj= classname
# obj.print()
'''''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        return f"helow my name is {self.name} and my age is {self.age}." 
obj=Person("prabesh",22)
print(obj.greet())
           
'''''''''''''
# single inheritance
class Animal:
    def eat(self):
        print("animal can eat")
    def walk(self):
        print("amimal can walk")

class Dog(Animal):
    def bark(self):
        print("dogs can bark")

obj=Dog()
obj.bark()
obj.eat()
obj.eat()
'''''''''''''
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} can walk!"

class Goat(Animal):
    def speak(self):
        return f"{self.name} says meey!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

goat = Goat("Fulmati")
cat = Cat("Tommy")

print(goat.speak())  
print(cat.speak())
print(goat.walk())
print(cat.walk())
'''''
'''''
#multiple inheritance
class Bike:
    def __init__(self, name):
        self.name = name

    def two_wheel(self):
        return f"{self.name} have two wheels "

class Car:
    def __init__(self, name):
        self.name = name
    def four_wheel(self):
        return f"{self.name} have 4 wheels"

class Truck:
    def __init__(self, name):
        self.name = name
    def six_wheel(self):
        return f"{self.name} have 6 wheels" 
class Vechicle(Bike,Car,Truck):
    def __init__(self, name):
        self.name = name
    def wheel(self):
        return f"{self.name} have wheels"
v=Vechicle("gaddi")
bike=Bike("pulser")
car=Car("furtuner")
truck=Truck("volvo")
print(bike.two_wheel())
print(car.four_wheel())
print(truck.six_wheel())
print(v.wheel())
print(v.two_wheel())
print(v.six_wheel())
'''''
'''''''''
#multilevel inheritance

class Vechicle():
    def __init__(self, name):
        self.name = name
    def wheel(self):
        return f"{self.name} have wheels"
class Bike(Vechicle):
    def __init__(self, name):
        self.name = name
    def petrol(self):
        return f"{self.name} need petrol"
class Pulser(Bike):
    def __init__(self, name):
        self.name = name
    def blue(self):
        return f"{self.name} is blue"
pul=Pulser("model 20 pulser")
bike=Bike("blue pulser")  
vec=Vechicle("gaddii") 
print(pul.blue()) 
print(pul.petrol())
print(pul.wheel())
print(bike.petrol())
print(bike.wheel())
print(vec.wheel())
'''''
'''''''''
#Incaplution
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_age(self):
        return self.age
    def set_age(self,age):
        if(age>0):
            self.age=age
        else:
            print("invalid age")
Person= Person("prabesh",22)  
print("name=",Person.get_name())  
print("age=",Person.get_age())    
Person.set_name("raju")
Person.set_age(30)
print("Updated_name=",Person.get_name())  
print("Updated_age=",Person.get_age())  
'''''
'''''''''
#incapulation
class Shape:
    pass
class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*(self.r**2)
def c_Area(shape):
    return shape.area()
r=Rectangle(2,5)
c=Circle(5)
print("area of rectangle is:",c_Area(r))
print("area of circle is:",c_Area(c))   
'''''
'''''
#abstraction
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    
r=Rectangle(3,4)    
print("area is:",r.area())
'''''
'''''
#overloading
from multipledispatch import dispatch # type: ignore
class Calculator:
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)
    @dispatch(float,float,float)
    def add(self,a,b,c):
        print(a+b+c)

o=Calculator()
o.add(3,6) 
o.add(4,6,8)
o.add(2.4,4.6,4.7)
        '''''
'''''''''
class Animal:
    def sound(self):
        return "generic sound"
class Dog(Animal):
    def sound(self):
        return " baRK"
class Cat(Animal):
    def sound(self):
        return "meou"
dog=Dog()
cat=Cat()
print(dog.sound())
print(cat.sound())    

#method overloading using defult parameter
class Calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
calc=Calculator()
print(calc.add(1,2))
print(calc.add(1,2,3))
print(calc.add(5)) 
'''''
'''''
#enceptional

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

'''''
'''''''''
#operator overloading
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"vector{self.x},{self.y}"

v1=Vector(3,4)    
v2=Vector(4,6)
v3=Vector(3,5)
v4=v1+v2
v5=v3+v1
print(v4)
print(v5)
'''''''''

#acess modifer
#protected=_ and private=__
'''''
#protected
class Animal:
    def __init__(self,species):
        self._species=species
    def display_species(self):
        print(f"species:{self._species}")

class Dog(Animal):
    def __init__(self,species,name):
        self._species=species
        self.name=name
    
    def display_info(self):
        print(f"name:{self.name}")
        print(f"species:{self._species}")

dog=Dog("kutta","rockey")
dog.display_species()
dog.display_info()
'''''
'''''
#private
class Animal:
    def __init__(self,species):
        self.__species=species
    def display_species(self):
        print(f"species:{self.__species}")

class Dog(Animal):
    def __init__(self,species,name):
        self._species=species
        self.name=name
    
    def display_info(self):
        print(f"name:{self.name}")
        print(f"species:{self._species}")

dog=Dog("kutta","rockey")
ani=Animal("janwaar")
#dog.display_species()
ani.display_species()
dog.display_info()
'''''
'''''
#abstract class
from abc import ABC,abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def sub(self,a,c):
        pass
class Simplecalc(Calculator):
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

sc=Simplecalc()
print("addition is",sc.add(9,4))
print("subtraction is",sc.sub(9,4))
'''
#Enumeration
from enum import Enum
class Direction(Enum):
    north=1
    south=2
    east=3
    west=4

print(Direction.north)
print(Direction.west.value)
for dir in Direction:
    print(dir.value)
if Direction.north==Direction.west:
    print("same direction")    
else:
    print("difference direction")
'''

#class var vs instanve var and 

class Circle:
    #class variable
    pi=3.14156

    def __init__(self,r):
        self.r=r   #inatance variable

    def calculate_area(self):
        return Circle.pi*self.r*self.r
    
    @classmethod
    def from_diameter(cls,d):
        r=d/2
        return cls(r)
    
c=Circle(5)    
c2=Circle.from_diameter(20)
a1=c.calculate_area()
a2=c2.calculate_area()
print("area of 1st circle is::",a1)
print("area of 2nd circle is::",a2)

'''''
'''''

#static method
class Calc:
    @staticmethod
    def add(x,y):
        return x+y
        '''''
'''''''''
#Destructer
class Car:
    def __init__(self,brand):
        self.brand=brand
        print(f"{self.brand} car created")

    def display(self):
        print(f"car brand:{self.brand}")

    def __del__(self):
        print(f"{self.brand} car deleted")
car1=Car("Tarjen")    
car2=Car("farari")
car1.display()
car2.display()
del car1
'''''    