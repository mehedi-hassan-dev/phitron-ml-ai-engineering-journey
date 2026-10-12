"""
 problem : Take an integer N. Print Even if N is even, otherwise print Odd. Use the modulus operator %. 

 Sample Input: 17 
 Sample Output: Odd
 """

number = int(input())

if number % 2 == 0:
    print("Even")
else:
    print("Odd")