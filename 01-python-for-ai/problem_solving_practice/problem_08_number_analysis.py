"""
Problem : Number Analysis

You are given N positive integers.
For each number:
If the number is even, ignore it and move to the next number.
If the number is odd, calculate the sum of its digits.
If the digit sum is greater than 20, stop processing any more numbers.
Otherwise, print the number and its digit sum.
At the end, print how many odd numbers were successfully processed.

Sample Input
6
12 135 47 91 999 25

So the output will be:
135 9
47 11
91 10
3
"""



N = int(input())

numbers = list(map(int, input().split()))

count = 0

for num in numbers:
    if num % 2 == 0:
        continue

    digit_sum = sum(int(digit) for digit in str(num))

    if digit_sum > 20:
        break

    print(num,digit_sum)

    count += 1

print(count)






# Bikolpo vabe problem solve

N = int(input())

numbers = list(map(int, input().split()))

count = 0
stope = False

for num in numbers:
    if num % 2 == 0:
        continue

    digit_sum = 0

    for dig in str(num):
        digit_sum += int(dig)

    if digit_sum > 20:
        stope = True
        break

    print(num, digit_sum)

    count += 1
print(count)
