"""
Problem: The Homework Bot (Easy)
Problem statement
The lab built a homework bot. It does not give long speeches. It only answers one question: did this student pass the AI quiz?
Write a function check_pass(marks) that returns True if marks >= 40, otherwise False. Do not print inside the function. 
Add a short docstring — even bots deserve documentation.
Then read one quiz mark, call the function, and print Pass or Fail.

Input
One line: an integer marks (−100 ≤ marks ≤ 100).
Output
Print Pass or Fail.

Examples
Input
73
Output
Pass

Input
39
Output
Fail
"""

# Problemer statement anujai True ,False return korbe then function er bahire print korbe pass or fail

def check_pass(marks):

    """Return True if the student passed, otherwise False."""   # Docstring

    return marks >= 40

marks = int(input())


if check_pass(marks):

    print("Pass")
else:
    print("Fail")





# Bikolpo vabe solve . But akhane True , False return korbe na . akhane return korbe Pass or Fail


def check_pass(marks):

    """Return True if the student passed, otherwise False."""  # Docstring

    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


result = check_pass(int(input()))

print(result)