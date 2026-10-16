"""
Problem: Sum Digits
time limit per test2 seconds
memory limit per test256 megabytes
Given a number N and an array A of N digits (not separated by space). Print the summation of these digits.

Input
First line contains a number N (1  ≤  N  ≤  106) number of digits.

Second line contains N digits (0 ≤ Ai ≤ 9).

Output
Print the summation of these digits.

Example
Input
5
13305

Output
12

Note
First Example :

1 + 3 + 3 + 0 + 5 = 12 .


"""



n = int(input())
numbers = input()

total_sum = sum(int(num) for num in str(numbers))

print(total_sum)





# Bikolpo vabe solve 

n = int(input())
numbers = input()

total_sum = 0
for i in str(numbers):
    total_sum += int(i)
print(total_sum)