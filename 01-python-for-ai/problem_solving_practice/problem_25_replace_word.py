"""
Problem: Replace Word

Given a string S. Print S after replacing every sub-string that is equal to "EGYPT" with space.

Input
Only one line contains a string S
 (1≤|S|≤103)
 where |S| is the length of the string and it consists of only uppercase English letters.

Output
Print the result as required above.

Examples
InputCopy
BRITISHEGYPTGHANA

Output
BRITISH GHANA

Input
ITALYKOREAEGYPTEGYPTALGERIAEGYPTZ

Output
ITALYKOREA  ALGERIA Z

"""


# Replace method use kore akdom easy vabe solve
S = input()

print(S.replace("EGYPT" , " "))






# Bikolpo vabe solbe . akhane while loop use kore solve kora hoyese
s = input()

result = ""
i = 0

while i < len(s):
    if s[i:i+5] == "EGYPT":
        result += " "
        i += 5

    else:
        result += s[i]
        i += 1

print(result)