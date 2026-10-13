# open() use kore file handling
# write mood use kore file create korlam

file = open("file-handling-example.txt", "w")
writ = file.write("Hello Python\nI am learning file handling\nPython is useful")
file.close()



# open() method use kore file read kora

file = open("file-handling-example.txt", "r")
red = file.read()
# akhane "red" ke print korle file er text print hobe , ami akhane print avoid korci karon akoi content niche print korci, akhane print korle sem text bar bar dekhabe



# with use kore file handlihg. with use korle file auto closed hoi . Best practice holo with use kora

# with use kore file ea new line append kora hoise

with open("file-handling-example.txt", "a") as file:
    file.write("\nFile handling is most usefull topic")



# with use kore file read

with open("file-handling-example.txt", "r") as file:

    red1 = file.read()

    print(red1)



# puro content valu print na kore kisu value print kora

with open("file-handling-example.txt", "r") as file:
    content = file.read(5)
    print(content)



# readline() method >- akbare akti line read kore

with open("file-handling-example.txt", "r") as file:

    print(file.readline()) # ei methode ea  every line print er por akti new line add hoi
    print(file.readline())



# new line remove kore

with open("file-handling-example.txt", "r") as file:

    print(file.readline(),end="") # ei methode new line remove kore print kore
    print(file.readline(),end="")



# readlines() method >- file er every line read kore list hisebe print kore

with open("file-handling-example.txt", "r") as file:

    print(file.readlines())



# List theke Every line alada kore print korte

with open("file-handling-example.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line, end="")



# Boro file(4/6 GB) puro load na kore ei method use kore file load kora valo . akkhete puro file aksathe memory te rakte hoi na hoi na

with open("file-handling-example.txt", "r") as file: # Boro file  er junno usefull

    for line in file:
        procesed_line = line.strip()
        print(procesed_line)




#-----------------File Pointer-----------


# tell() method  >- current file pointer position indicate kore।

with open("file-handling-example.txt", "r") as file:
    print(file.tell())
    file.read(10)
    print(file.tell())



# seek() method >- use kore file pointer er obsthan poribotton kora jai

with open("file-handling-example.txt", "r") as file:
    file.seek(27)
    print(file.tell())
    print(file.read())


with open("file-handling-example.txt", "r") as file:
    print(file.read(5)) # akhon file pointer 5 index ea ase
    print(file.tell())
    file.seek(0)      # seek use kore file pointer ke 0 index ea ana holo
    print(file.tell())
    
    


#-------------Exceptions Handling part-----------


# try and except example

try:
    number = int(input("Enter a first number: ")) # akhanne intiger valu betito onno value input dile ValueError hobe
    print(number)
except ValueError:
    print("Please enter a valid integer.")




# else block  >- tokhon execute hoi jokhon try block ea kono except hoi na 
try:
    number = int(input("Enter a Second number: "))
except ValueError:
    print("Invalid number.")
else:
    print("Your number is:", number)




# finally block >- usually try block ea excrption hok ba na hok last ea execute hobe
try:
    number = int(input("Enter a third number:"))
except ValueError:
    print("Value error")
finally:
    print("Execution finished.")