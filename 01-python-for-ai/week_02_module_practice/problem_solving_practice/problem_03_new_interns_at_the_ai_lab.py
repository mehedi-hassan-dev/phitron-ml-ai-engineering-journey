"""
Problem: New Interns at the AI Lab 

Problem statement
Two new interns just walked in. Security will not open the GPU room without an ID card. Your job is the card printer.
Write student_card(name, roll, dept) that prints:
<name> | Roll: <roll> | Dept: <dept>

You will get two interns. Call the function twice with positional arguments: name, then roll, then dept. 
Swap the order and someone from EEE will get into the CSE GPU queue. Chaos.

Input
Two lines. Each line: name roll dept (name and dept are one word).
Output
Two ID lines, same order as input.

Example:
Input
Rafi 101 CSE
Mim 102 EEE

Output
Rafi | Roll: 101 | Dept: CSE
Mim | Roll: 102 | Dept: EEE
"""


def student_card(name, roll, dept):

    print(f"{name}  |  Roll: {roll}  |  Dept: {dept}")


for _ in range(2):

    name, roll, dept = input().split()


    student_card(name, roll, dept)

