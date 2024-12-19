class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name from Parent: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        super().show()  # Calls the show method from Parent class
        print(f"Age from Child: {self.age}")

# Creating an object of Child class
child = Child("John", 25)
child.show()
