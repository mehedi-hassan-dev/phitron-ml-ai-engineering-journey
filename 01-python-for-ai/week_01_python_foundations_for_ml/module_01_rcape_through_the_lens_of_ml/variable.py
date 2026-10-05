a = 20
print(a)
print(type(a))


b = 3.14
print(b)
print(type(b))


a = b # akhane b er value ke a er sathe assign korlam
print(a)
print(type(a))


c = "Mehedi Hasan"
print(c)
print(type(c))


data = input("Enter your name: ")
print(data)
print(type(data))


a = input("Enter a value: ") # input() function always returns a string
print(a)
print(type(a))


a = int(input("Enter a value: ")) # a ke type casting er maddhome integer e convert korlam
print(a)
print(type(a))


row_num = input("Enter the number of rows: ")

numbers = row_num.split() # split() function er maddhome string ke list e convert korlam
a = int(numbers[0]) # list er prothom element ke a te assign korlam
print(a)
print(type(a))

b = int(numbers[1]) # list er ditiyo element ke b te assign korlam
print(b)
print(type(b)) 
print("The sum of a and b is: ", a + b) # a and b er sum print korlam