"""
Problem: Lowest Number

time limit per test1 second
memory limit per test256 megabytes
Given a number N and an array A of N numbers. Print the lowest number and its position.

Note: if there are more than one answer print first one's position.

Input
First line contains a number N (2 ≤ N ≤ 1000) number of elements.

Second line contains N numbers (-105  ≤  Ai  ≤  105).

Output
Print the lowest number and its position (1-index).

Examples
Input
3
1 2 3
Output
1 1

Input
5
5 6 2 3 2
Output
2 3
"""


N = int(input())

numbers = list(map(int, input().split()))

lowest = numbers[0]
position = 1

for i in range(1, N):

    if numbers[i] < lowest:
        lowest = numbers[i]
        position = i + 1


print(lowest,position)





# Bikolpo vabe Solve min function use kore

n = int(input())
numbers = list(map(int, input().split()))

lower_num = min(numbers)

position = numbers.index(lower_num) + 1
print(lower_num, position)