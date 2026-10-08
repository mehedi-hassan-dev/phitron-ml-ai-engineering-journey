# Given N numbers. Count how many of these values are enen, odd, positive and negative.
# Simple input N = 5 
#             -5 0 -3 -4 12
# output :
# Even: 3
# Odd: 2
# Positive: 1
# Negative: 3

N = int(input())
numbers = list(map(int, input().split()))

even = 0
odd = 0
positive = 0
negative = 0

for x in numbers:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1

    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)