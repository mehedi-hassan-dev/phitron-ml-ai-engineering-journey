# Function Structure
def function_name(parameters):
    """Optional documentation"""
    # Function body
    result = parameters
    return result


# Function call kora hoi ni
def my_function():
  print("Hello from a function")


# function use kore 2 number add
def add(a, b):
    return a + b

print(add(30, 40))
result = add(10, 20)
print(result)


# function execute 
def greet():
    print("Good Morning!")

greet() # greet call korer por function execute hoi


# function ea argument pass
def multiply(a, b): # akhane a,b holo parameters
    return a * b # return folafol ferot dey. and a*b calculation kore

result = multiply(5, 4) # 4,5 holo argument 
print(result)


# Function ea Default parameter uses
def greet(name="Student"):
    print(f"Hello, {name}!")

greet() # akhane argument dewa hoi ni ta default hisebe student print korse
greet("Mehedi") # akhane Mehedi argument pass kora hoise ta mehedi print korse


# Function ea positional arguments er uses
def student_info(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)

student_info("Mehedi", 21, "CSE")


# Function ea keyword arguments er uses
def student_info(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)

student_info(
    age=25,
    department="Civil",
    name="Hassan"
)


"""Function ea 2 dhoroner arguments aksathe uses
 tobe positional argument age hobe er por keyword arguments hobe"""

def introduce(name, age, city):
    print(name, age, city)

introduce("Mehedi", age=21, city="Dhaka")


# Function ea print() kivabe kaj kore
def add(a, b):
    print(a + b) # print sudhu result print kore kono value retun kore na

result = add(10, 20)
print("Result:", result) # None type hobe karon value return kore ni


# Function ea retun kivabe kaj kore
def add(a, b):
    return a + b # retun value return kore ei junno result print hobe

result = add(10, 20)
print("Result:", result)


# Function ea multiple value return
def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(10, 5)

print("addition:",addition)
print("subtraction:",subtraction)
print("multiplication:",multiplication)


#Function Documentation ba Docstring
def calculate_area(length, width):
    """Calculate the area of a rectangle.""" # Dogstring
    return length * width

print(calculate_area(5, 3))
print(calculate_area.__doc__)



# Iterator and Generator

# iterable
numbers = [10, 20, 30]

for number in numbers:
    print(number)


#terator
numbers = [40, 50, 60]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Generator
def count_numbers():
    yield 1
    yield 2
    yield 3

numbers = count_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))


# Lambda, Map and Apply Function

# Normal function
def square(x):
    return x * x

print(square(5))

# lambda function 
square = lambda x: x * x

print(square(5))


# lambda function ea multiple paramete use
add = lambda a, b: a + b

print(add(10, 20))


# Conditional expression use kore Lambda function
check = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check(4))
print(check(7))


# simple loop use kore squire print
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

print(squares)

# map use kore squire
numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n

result = map(square, numbers)

print(list(result))


# lambda & map ak sahte use squire
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)