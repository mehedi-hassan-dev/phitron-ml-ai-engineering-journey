# String print
print("Hello")


# variable ea string assing
name = "Md. Mehedi Hassan"
print(name)


# Multiline Strings
a = """Hello how are
Nice to meet you
meet you too
"""
print(a)


# String indexing
name = "Mehedi"

print(name[0])
print(name[1])
print(name[-1])
print(name[-2])


# string slicing
name = "Mehedi Hassan"

print(name[0:6])
print(name[7:])
print(name[:6])
print(name[-6:])
print(name[::2])


# String concatenation
first_name = "Mehedi"
last_name = "Hassan"

full_name = first_name + " " + last_name

print(full_name)


# String repetition
text = "Python "

print(text * 3)


# String er lenth print kora
name = "Mehedi"

print(len(name))


# if statement use
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# not in er use
txt = "The best things in life are free!"
print("expensive" not in txt)


# String methods
# lower and upper method
text = "Machine Learning"

print(text.upper())
print(text.lower())


# strip method >- strom er start & end er white space remove kore
text = "   Hello World   "

print(text.strip())


# replace() method  >- akti substring ke onno akti substring diye replace kora
text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)


# find() >- substring prothom kon index ea ase ta dey na thakle -1 dey
text = "Machine Learning"

print(text.find("Learning"))
print(text.find("Deep Learning"))


# count() >- akti substring kotobar ase tar count dey
text = "banana"
print(text.count("a"))


# startswith() and endswith() method
filename = "report.pdf"

print(filename.startswith("report"))
print(filename.endswith(".pdf"))

# in operato >- kono substring string er vitor ase ki na ta chek kore
text = "Machine Learning"

print("Deep Learning" in text)
print("Learning" in text)


# split() >- string ke list ea convert kore
text = "Machine Learning Artificial Intelligence"

words = text.split()

print(words)
print(type(words))


# join() >- holo split er ulta ati list er string ke jora lagai
words = ["Machine", "Learning"]
text = "".join(words)

print(text)

# coma use kore string join
languages = ["Python", "Java", "C++"]
text = ",".join(languages)

print(text)


# String comparison
name1 = "Python"
name2 = "Python"

print(name1 == name2)


# f-string formatting
name = "Mehedi"
age = 22

print(f"My name is {name} and I am {age} years old.")


# f-string er vitor expression use kora 
a = 10
b = 5

print(f"Sum: {a + b}")


# decimal formate
cgpa = 3.75682

print(f"CGPA: {cgpa:.2f}")


#\n use kore new line print
print("Line 1\nLine 2")
