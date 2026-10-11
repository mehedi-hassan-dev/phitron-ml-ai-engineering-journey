# sets 
fruits = {"apple", "banana", "mango"}
print(fruits)
print(type(fruits))


# Empty set create
em_set = set()
print(type(em_set))


# Sets duplicate value accept kore na
numbers = {10, 20, 20, 30, 30}
print(numbers)


# set ea element add kora
fruits = {"stobry", "banana"}
fruits.add("mango")

print(fruits)


# update method use kore multiple element add kora
fruits = {"jackfruit", "banana"}
fruits.update(["coconut", "orange"])

print(fruits)


# set er element remove kora 
flowers = {"Rose", "Lily", "Louts"} # element na thakle error hobe example flowers.remove("hasnahena")
flowers.remove("Lily")

print(flowers)


# discard() method use kore element remove kora
fruits = {"apple", "banana", "mango"} # element na thakle error hobe na example fruits.discard("coconut")
fruits.discard("banana")

print(fruits)


# pop() method use kore element remove kora
numbers = {12, 22, 44, 66}
removed = numbers.pop()

print(removed)
print(numbers)


# clear() method use kore puro set er items ke remove kora hoi
fruits = {"apple", "banana", "mango"}
fruits.clear()

print(fruits)


# in use kore Membership Check 
fruits = {"apple", "banana", "mango"}

print("apple" in fruits)
print("grape" in fruits)


# set ea loop bebohar
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)



# sets operation
# union()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
new_set = a.union(b)
print(new_set)


# intersection()
a = {11, 22, 33, 44}
b = {33, 44, 55, 66}
int_set = a.intersection(b)
print(int_set)


# difference
c = {55, 66, 77, 88}
d = {99, 77, 22}

dif_set = c.difference(d)
print(dif_set)


# Subset and 
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))


#Superset
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issuperset(b))