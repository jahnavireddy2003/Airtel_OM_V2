# Program to print a right-angled triangle (rectangle triangle) using stars

height = int(input("Enter the height of the triangle: "))

for i in range(1, height + 1):
    print('*' * i)