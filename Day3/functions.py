import module as md
def func():
  print("Hello world")

func()
def func2(name, age = 24):
  print(name, age)

func2("Shruti")

def func3(*names):
    print(names)

func3("Shruti", "Dhriti")

def func4(**names):
    print(names["lname"])
    return names["age"]*2

print(func4(fname = "Shruti", lname = "Sharma", age = 24))

def func5(numbers):
    md.hello_func("ABC")
    print(numbers)
numbers = [1,2,3,4,5]
func5(numbers)
