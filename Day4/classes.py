class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def disp(self):
        print("Hello "+ self.name)
obj = Test("Shruti", 23)
obj.disp()
print(obj.name)
print(obj.age)

class Child(Test):
    pass
ob = Child("Dhriti", 4)
ob.disp()

class Child2(Test):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year
    def __str__(self):
        return f"{self.name} is {self.age} years old In child class"
    def greet(self):
        print("Good Morning", self.name, self.year)
obj1 = Child2("XYZ", 15, 2009)
obj1.greet()
obj1.disp()
print(obj1)
print(type(obj1))