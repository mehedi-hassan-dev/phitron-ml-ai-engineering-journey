"""
Problem: Take a string as input. Count how many vowels it has (a, e, i, o, u in both lowercase and uppercase) 
using a loop. Print only the count. 

Sample Input: Education 
Sample Output: 5
"""


string = input()

voewels = "aeiouAEIOU"
count = 0

for char in string:
    if char in voewels:
        count += 1
print(count)