"""
Problem: You are given a list of marks: [90, 40, 75, 88, 35]. For each mark, print the mark and Pass
if it is at least 40, otherwise Fail. Then print how many students passed and the average of all marks.
  
Sample Input: No input Sample 
Output: 90 Pass 40 Pass 75 Pass 88 Pass 35 Fail Passed: 4 Average: 65.6
"""



marks = [90, 40, 75, 88, 35]

pass_count = 0
total_mark = 0


for mark in marks:
    total_mark += mark

    if mark >= 40:
        pass_count += 1

        print(mark,"Pass",end=" ")
    else:
        print(mark,"Fail",end=" ")

avarage = total_mark/len(marks)


print(f"Passed: {pass_count} Average: {avarage}")
