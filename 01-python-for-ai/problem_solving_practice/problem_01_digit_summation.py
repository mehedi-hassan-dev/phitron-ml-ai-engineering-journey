# Given two numbers N and M . print the summation of their last digit
# input formate 12 15
# output hobe 7

num = input() 

numbers = num.split() # split method use kore string ke list ea convert korlam

x = int(numbers[0]) # str ke intiger ea convert korlam
y = int(numbers[1])

last_digit_of_x = x % 10 # akhane number er sathe 10% kore last digit ber korlam 
last_digit_of_y = y % 10

sum = last_digit_of_x + last_digit_of_y

print(sum)