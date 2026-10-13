"""
Problem: J. Count Letters
time limit per test2 seconds
memory limit per test64 megabytes
Given a string S. Determine how many times does each letter occurred in S.

Input
Only one line contains the string S (1 ≤ |S| ≤ 107) where |S| is the length of the string and it consists of only lowercase English letters.

Output
For each character that appears in S, print a single line that contains the following format: "X : Y" where X is the letter and Y is the number of times that letter X occurred in S.

Note: you must print letters in ascending order.

Input
aaabbc

Output
a : 3
b : 2
c : 1

Input
regff

Output
e : 1
f : 2
g : 1
r : 1

"""

# simple vabe solve

S = input()

for ch in sorted(set(S)):
    count = S.count(ch)

    print(f"{ch} : {count}")




# Bokolpo niyom ea problem solve
# efficient code structure time complexity kom

s = input()


freq = [0]* 26

for ch in s:
    index = ord(ch) - ord("a") # Python er ord() function akti character er Unicode code point dey.
    freq[index] += 1

for i in range(26):
    if freq[i] > 0:

        print(f"{chr(i + ord("a"))} : {freq[i]}")




