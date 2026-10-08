# Given 3 numbers A,B and C, Print the minimum and the maximum   numbers
# Simple Input 1 2 3  Output 1 3
# Simple Input -1 -2 -3 Output -3 -1
# Simple Input 10 20 -5 Output -5 10

num = input()

numbers = num.split()

x = int(numbers[0])
y = int(numbers[1])
z = int(numbers[2])

min = x
max = x

if y < min:
    min = y
if z < min:
    min = z

if y > max:
    max = y
if z > max:
    max = z

print(min, max)