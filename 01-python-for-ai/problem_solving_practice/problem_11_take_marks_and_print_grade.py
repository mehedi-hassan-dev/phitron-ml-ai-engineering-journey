""" Problem: Take an integer marks. Print the grade using this rule, and put the highest check 
first: A+ if marks >= 80, A if marks >= 70, Pass if marks >= 40, otherwise Fail. 

Sample Input: 85 Sample Output: A+ Sample Input 2: 40 Sample Output 2: Pass"""


marks = int(input())

if marks >= 80:
    print("A+")

elif marks >= 70:
    print("A")

elif marks >= 40:
    print("Pass")

else:
    print("Fail")