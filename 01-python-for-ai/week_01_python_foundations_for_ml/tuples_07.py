# tuples

tup = (1,2,3,4)
print(type(tup))


# empty tuple
tup = ()
print(type(tup))


# different values tuples

fruits = ("apple", "banana", "mango") # string value tuple
numbers = (10, 20, 30) # int value tuple
mixed = ("Mehedi", 21, True) # mixed value tuple

print(fruits)
print(numbers)
print(mixed)


# Parenthesi use na kore tuple create kora 

tup = 23, 25
print(tup)
print(type(tup))


# single element ke tuple korte hole element er pore coma dite hobe 

a = (5,)    
b = (5)    
print(type(a))  # <class 'tuple'>
print(type(b))  # <class 'int'>


# index use kore element dekha 

fruits = ("apple", "banana","cheery", "mango")

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # mango


# tuple slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])   # (20, 30, 40)
print(numbers[:3])    # (10, 20, 30)
print(numbers[2:])    # (30, 40, 50)
print(numbers[::-1])  # (50, 40, 30, 20, 10)


# Tuples method 
# count()

numbers = (10, 20, 30, 20, 40)
print(numbers.count(20))   # 2

# index()

numbers = (10, 20, 30, 22, 44, 20, 40)

print(numbers.index(44))   # 4


# Tuple Unpacking (condition holo variable size soman value size hote hobe)

person = ("Mehedi", 21, "Dhaka")
name, age, city = person

print(name)  # Mehedi
print(age)   # 21
print(city)  # Dhaka


# tuple er upor loop chalano

fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)