
# Empty list

numbers = []
print(numbers)


# Integer list

marks = [85, 90, 78, 95]
print(marks)


# String list

languages = ["Python", "Java", "C++"]
print(languages)


# Mixed data type list

student = ["Mehedi", 22, 3.75, True]
print(student)


# indexing use kore list er element access kora

fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana


# negative indexing use kore list er element access kora

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  # Output: cherry


# list er element change kora

fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']


# list er element add kora

names = ["Mehedi", "Hasan"]
names.append("Rahim")
print(names)  # Output: ['Mehedi', 'Hasan', 'Rahim']


# list er element remove kora

books = ["Python", "Java", "C++"]
books.remove("Java")
print(books)  # Output: ['Python', 'C++']  



# list er element pop kora

numbers = [1, 2, 3, 4, 5]
numbers.pop() 
print(numbers)  # Output: [1, 3, 2, 4]


# list er element clear kora

birds = ["sparrow", "eagle", "parrot"]
birds.clear()
print(birds)  # Output: []  


# list er length ber kora

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5


# in operator use kore list er element check kora

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is in the list")



# list er upor for loop use kora

flowers = ["rose", "lily", "tulip"]
for flower in flowers:
    print(flower)


# list comprehension use kore list create kora

squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25] 


# list slicing

numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]


# list er last 3 element access kora

numbers = [1, 2, 3, 4, 5]
print(numbers[-3:])  # Output: [3, 4, 5]


# list er first 3 element access kora

numbers = [11, 22, 33, 44, 55]
print(numbers[:3])  # Output: [11, 22, 33]

# list er element reverse kora

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]   


# list er element sort kora

numbers = [51, 23, 94, 14, 52, 60]
numbers.sort()
print(numbers)  # Output: [14, 23, 51, 52, 60, 94]


# list er element sort kora (descending order)

numbers = [51, 23, 94, 14, 52, 60]
numbers.sort(reverse=True)
print(numbers)  # Output: [94, 60, 52, 51,23, 14]


# list er element copy kora

numbers = [1, 2, 3, 4, 5]
new_numbers = numbers.copy()
print(new_numbers)  # Output: [1, 2, 3, 4, 5]   


# list er element extend kora

numbers1 = [11, 12, 13]
numbers2 = [14, 15, 16]
numbers1.extend(numbers2)
print(numbers1)  # Output: [11, 12, 13, 14, 15, 16]


# list er element insert kora     

names = ["Mehedi", "Hasan"]
names.insert(1, "Rahim")
print(names)  # Output: ['Mehedi', 'Rahim', 'Hasan']        


# list er element index ber kora

fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # Output: 1


# list theke kono akti element count kora

books = ["Python", "Java", "C++", "Python"]
count = books.count("Python")
print(count)  # Output: 2   

# nested list 

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)  # Output: [[1, 2, 3], [4, 5, 6]] 


# nested list theke element access kora

students = [
    ["Mehedi", 85],
    ["Rahim", 90],
    ["Karim", 78]
]

print(students[0])
print(students[0][0])
print(students[1][1])


# list er upor while loop use kora

numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1     


# condition use kore list comprehension

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]     
