""" Given a number N. Print the digits of that from right to left separated by space

simple input N = 4
             121
             39
             123456
             1200

        output:
              1 2 1
              9 3
              6 5 4 3 2 1
              0 0 2 1
"""

N = int(input())

for i in range(N):
    numbers = int(input())

    if numbers == 0:
        print(numbers)

        continue

    while numbers > 0:
        print(numbers % 10, end=" ")
        numbers //= 10
    print()