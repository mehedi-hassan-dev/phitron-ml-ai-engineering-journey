"""
Problem: Three Training Runs 
Problem statement
You trained a tiny model three times. Same data, three different random seeds. The accuracies came out different — models have moods,
like you before coffee.
Write average(a, b, c) that returns the mean accuracy as a float: (a + b + c) / 3. Call it with positional arguments and print only the returned value. 
The report needs a decimal, so the supervisor believes you actually divided.

Input
One line: three numbers a b c (the three accuracies).
Output
Print the average as a float (for example 20.0, not 20).

Example
Input
10 20 30

Output
20.0
"""



def average(a, b, c):

    return (a + b +c) / 3

a, b, c = (map(int, input().split()))

print(average(a, b, c))