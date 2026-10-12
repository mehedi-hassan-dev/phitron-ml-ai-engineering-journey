"""
problem:
Take two integers using input() and print their sum. Remember: input() always returns a string,
 so convert with int() before adding.

 Sample Input: 5 2 
 Sample Output: 7"""


# map function use kore sum calculation

num1,num2 = list(map(int, input().split()))

result = num1 + num2

print(result)




# List comprehension use kore sum calculation

total_sum = sum([int(num) for num in input().split()])
print(total_sum)




# Loop use kore sum calculation

N = input().split()
add = 0

for num in N:
    add += int(num)
    
print(add)