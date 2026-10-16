"""
Problem: Good or Bad

Given a string S. Determine whether this string is Good or Bad.
Note: The string is Good if and only if it has "010" or "101" as one of its sub-strings and it's not necessary to have both of them.
A substring of a string is a contiguous subsequence of that string. So, string "forces" is substring of string "codeforces", but string "coder" is not.

Input
The first line contains a number T (1 ≤ T ≤ 100) number of test cases.
Each of the T following lines contains a string S (1 ≤ |S| ≤ 105) where |S| is the length of the string..
It's guaranteed that S contains only '1s' and '0s'.

Output
For each test case, print "Good" if the string is Good otherwise, print "Bad".

Example
Input
2
11111110
10101010101010

Output
Bad
Good

Note Example case 1:
The string doesn't contain 010 or 101 as sub-strings.

Example case 2:
The string contains both 010 and 101 as sub-strings
"""




t = int(input())

for _ in range(t):
    s = input()

    if "010" in s or "101" in s:
        print("Good")
    else:
        print("Bad")





# Bikolpo vabe solve. akhane for loop use kore problem solve kora hoise

T = int(input())

for _ in range(T):
    S = input()
    found = False

    for i in range(len(S) - 2):
        part = S[i : i + 3]

        if part == "101" or part == "010":
            found = True
            break
    if found:
        print("Good")
    else:
        print("Bad")