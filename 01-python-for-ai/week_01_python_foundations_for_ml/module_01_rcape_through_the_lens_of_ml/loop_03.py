# for loop

for i in range(6):
    print(i)


# for loop ea range(start & stop) use example

for i in range(2, 6):
    print(i)


# for loop ea range(start, stop, step) use example

for i in range(4, 14, 2):
    print(i)


#  Reverse Loop

for i in range(10, 0, -1):
    print(i)


# String er upor for loop

name = "Mehedi"

for char in name:
    print(char)


# List er upor for loop

fruits = ["apple", "banana", "cherry"]  

for fruit in fruits:
    print(fruit)


# tuple er upor for loop

numbers = (1, 2, 3, 4, 5)

for num in numbers:
    print(num)


# set er upor for loop

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)


# dictionary er upor for loop

student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CST"
}

# only key print korar jonno for loop
for key in student:
    print(key)

# only value print korar jonno for loop
for value in student.values():
    print(value)

# key and value both print korar jonno for loop
for key, value in student.items():
    print(key, value)


# for loop er moddhe break statement use example

for i in range(10): # break statement er maddhome loop ke terminate kore dey
    if i == 5:
        break
    print(i)


# for loop er moddhe continue statement use example

for i in range(10,16): # continue statement er maddhome loop er current iteration skip kore next iteration e chole jay
    if i == 12:
        continue
    print(i)


# for loop er moddhe pass statement use example

for i in range(5): # pass statement placeholder hisebe kaj kore
    if i == 3:
        pass
    else:
        print(i)




# While loop

i = 1

while i <= 5:
    print(i)
    i += 1


# while loop er moddhe break statement use example

i = 1

while i <= 10:

    if i == 5:
        break

    print(i)
    i += 1