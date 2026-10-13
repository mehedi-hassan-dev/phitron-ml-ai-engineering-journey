"""
problem: Take a word as input. Print the first character, the last character, and the length, separated by spaces.
 
 Sample Input: Python 
 Sample Output: P n 6
 """


words = input()

first_char = words[0]
last_char = words[-1]
lenth = len(words)


print(first_char,last_char,lenth)