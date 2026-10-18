
# OOP er Class create

class Student:
    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept

    def show_info(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Dept: {self.dept}")


s1 = Student("Mehedi", 101, "CSE")
s2 = Student("Rafi", 102, "EEE")

s1.show_info()
s2.show_info()




# ------------------Inheritance----------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, roll, dept):
        super().__init__(name, age)
        self.roll = roll
        self.dept = dept

    def show_student_info(self):
        print(f"Roll: {self.roll}, Dept: {self.dept}")


s1 = Student("Hassan", 25, 420, "CST")
s1.introduce()
s1.show_student_info()

s2 = Student("Babu", 22, 240, "TEXT")

s2.introduce()
s2.show_student_info()




# -------------------Polymorphism---------------

class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()




# Inheritance- er sathe Polymorphism

class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.speak()




# --------------Encapsulation-----------------

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Mehedi", 2000)
print(account.get_balance())

account.deposit(500)
print(account.get_balance())




# Getter ও Setter
# Private data porar junno getter, and condition anujai data change korer junno setter use kora hoi

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


s1 = Student("Mehedi", 85)

print(s1.get_marks())

s1.set_marks(95)
print(s1.get_marks())

s1.set_marks(150)




# ----------------Abstraction----------------

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


c = Circle(5)
r = Rectangle(4, 6)

print(c.area())
print(r.area())