"""
Problem: Replace MinMax

time limit per test1 second
memory limit per test256 megabytes
Given a number N and an array A of N numbers. Print the array after doing the following operations:

Find minimum number in these numbers.
Find maximum number in these numbers.
Swap minimum number with maximum number.
Input
First line contains a number N (2 ≤ N ≤ 1000) number of elements.

Second line contains N numbers ( - 105 ≤ Ai ≤ 105)

It's guaranteed that all numbers are distinct.

Output
Print the array after the replacement operation.

Example
Input
5
4 1 3 10 8

Output
4 10 3 1 8 

"""



N = int(input())
numbers = list(map(int, input().split()))

max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))

numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

print(*numbers) # akhane * use korai list er items gulo alada argument hisebe print ea jabe

