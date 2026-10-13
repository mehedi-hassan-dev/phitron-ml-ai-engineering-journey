"""
Problem: Keep taking integers as input. Add them to a total. Stop when a negative number appears (break).
Do not add that negative number. Then print the total. 
 
Sample Input: 4 8 15 -3 23 
Sample Output: 27 
 """

num = list(map(int, input().split()))
total = 0
for i in num:
    if i < 0:
        break
    total += i

print(total)