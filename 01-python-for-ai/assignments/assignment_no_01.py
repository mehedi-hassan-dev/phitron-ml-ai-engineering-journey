"""
Question No : 01

Given a list of integers, extract all numbers that are divisible by 4 but not divisible by 8.

Input Format:
Space-separated integers

Output Format:
A list of numbers satisfying the condition

Example:
Input:
4 6 8 12 16 20 24 28 

Output:
[4, 12, 20, 28] 
"""



# Answer to the Question No : 01

numbers = map(int, input().split())

new_lst = []

for num in numbers:
    if num % 8 == 0:
      continue
    if num % 4 == 0:
      new_lst.append(num)

print(new_lst)





"""
Question No : 02

Write a function compute_ratio(x, y) that returns (x + y) / (x * y). Use exception handling to manage division by zero.
Use exception handling to manage:
Division by zero

Input Format:
Two values

Output Format:
Computed result OR error message

Example:
Input:
5 0

Output:
Error: Division not possible
"""



# Answer to the Question No : 02

def compute_ratio(x, y):

  try:
    return (x + y)/ (x * y)
  except ZeroDivisionError:
    return "Error: Division not possible"

a,b = map(int,input().split())

print(compute_ratio(a,b))





"""
Question No : 03

Write a Python program that reads a text file and finds the longest word.

Requirements:

Open and read data from a file (Example: data.txt)
If multiple words have the same longest length, print any one of them

Input Format:
A text file containing multiple lines of text

Output Format:
The longest word

Example File Content (data.txt):
Python is a wonderful language for machine learning.

Output:
wonderful
"""



# Answer to the Question No : 03

with open("./sample_data/data.txt", "w") as file:
  file.write("Python is a wonderful language for machine learning")


with open("./sample_data/data.txt", "r") as file:
  string = file.read()
  words = list(map(str, string.split()))

  long_word = ""
  for word in words:
    if len(word) > len(long_word):
      long_word = word

  print(long_word)





"""
Question No : 04

Write a program that converts a sentence into a list of words 
but only includes words that start with a vowel (a, e, i, o, u), ignoring case.

Input Format:
A single line sentence

OutputFormat:
A list of strings

Example:
Input:
An apple a day keeps the doctor away

Output:
['An', 'apple', 'a', 'away']
"""



# Answer to the Question No : 04

word_list = list(map(str, input().split()))

vowel_char = "aeiouAEIOU"
start_vowel = []

for char in word_list:
  if char[0] in vowel_char:
    start_vowel.append(char)

print(start_vowel)





"""
Question No : 05

A word is called a Palindrome if reversing its letters results in the same word (ignoring case). 
Write a program to check whether a given string is a palindrome.

Input Format:
A single word string

Output Format:
"Palindrome" or "Not Palindrome"

Example:
Input:
Radar

Output:
Palindrome
"""



# Answer to the Question No : 05

word = input()
lower_word = word.lower()

reverse_word = lower_word[::-1]

if lower_word == reverse_word:
  print("Palindrome")
else:
  print("Not Palindrome")