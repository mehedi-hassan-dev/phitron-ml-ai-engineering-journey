# if conditional statement 

age = 20

if age >= 18:
    print("You are an adult")


# if-else conditional statement  

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# if-elif-else conditional statement

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade A+")
elif marks >= 70:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# nested if conditional statement

age = 20
has_id = False

if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("Please show your ID")
else:
    print("You cannot enter")



# multiple if-elif-else conditional statement

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")



# or conditional statement

day = "Friday"

if day == "Friday" or day == "Saturday":
    print("Weekend")
else:
    print("Working day")



# not conditional statement

is_raining = False  # not akti condition er result ulte dey

if not is_raining:
    print("You can go outside")



# in conditional statement

fruits = ["apple", "banana", "mango"]

fruit = input("Enter a fruit: ")

if fruit in fruits:
    print("Fruit is available")
else:
    print("Fruit is not available")


# ternary conditional statement

age = 20
status = "adult" if age >= 18 else "not adult"
print(status)

