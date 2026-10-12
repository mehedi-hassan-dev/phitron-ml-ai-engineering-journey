"""Problem: Take an integer N. Use a while loop to print numbers from 1 to N, each on a new line. 
Do not forget to increase the counter.

Sample Input: 5 Sample Output: 1 2 3 4 5"""



num = int(input())

count = 1

while count <= num:
    print(count)
    count +=1