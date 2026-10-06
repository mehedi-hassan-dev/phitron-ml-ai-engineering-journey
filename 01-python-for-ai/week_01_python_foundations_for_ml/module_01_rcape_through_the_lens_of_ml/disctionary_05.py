# Empty dictionary
student = {}

# Key-value dictionary
student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CSE",
    "cgpa": 3.75
}

print(student)

# Accessing values using keys

print(student["name"])  # Output: Mehedi    
print(student["age"])   # Output: 22
print(student["department"])  # Output: CSE
print(student["cgpa"])  # Output: 3.75


# get method use kore value access kora jay, jodi key na thake tahole default value return kore

student = {
    "name": "Mehedi",
    "age": 22
}

print(student.get("name"))
print(student.get("email"))
print(student.get("email", "Not found"))


# key value pair add kora 

student = {
    "name": "Mehedi",
    "age": 22
}

student["department"] = "CSE"

print(student)


# key value pair update kora

student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CSE"
}

student["department"] = "EEE"

print(student)


# update method use kore akadhik key value pair update kora ba add kora jay


student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CSE"
}         

student.update({
    "age": 25,
    "department": "Civil",
    "cgpa": 3.75
})

print(student)


# pop method use kore item delete kora

student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CSE"
}

removed_value = student.pop("department")

print(removed_value)
print(student)


# del method use kore item delete kora

student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CSE"
}

del student["age"]
print(student)


# clear method use kore dictionary clear kora

student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CSE"
}
student.clear()
print(student)


# keys, values & items method use kore dictionary er keys, values & items access kora

student = {
    "name": "Hassan",
    "age": 26,
    "department": "Textile"
}

print(student.keys())
print(student.values())
print(student.items())


# key er upore loop chalay dictionary er value access kora

student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CSE"
}

for key in student:
    print(key)

# Key value pair er upore loop chalay dictionary er value access kora

student = {
    "name": "Mehedi",
    "age": 22,
    "department": "CSE"
}

for key, value in student.items():
    print(key, ":", value)



# Nested dictionary

students = {
    "s1": {
        "name": "Mehedi",
        "cgpa": 3.75
    },
    "s2": {
        "name": "Rahim",
        "cgpa": 3.50
    }
}

print(students["s1"]["name"])
print(students["s2"]["cgpa"])