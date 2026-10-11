"""
Problem : Find the First Number Greater Than 100

You are given N integers.
Find the first number greater than 100.
As soon as you find the first number greater than 100,
stop checking the remaining numbers.

If there is no number greater than 100, print:
Not Found

Sample Input:
7
20 45 80 105 150 200 300

Sample Output:
105
"""


N = int(input())

numbers = list(map(int, input().split()))

found = False

for num in numbers:
    if num > 100:
        print(num)
        found = True
        break

if not found:
    print("Not Found")