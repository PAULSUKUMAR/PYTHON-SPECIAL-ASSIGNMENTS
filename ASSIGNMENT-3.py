#ASSIGNMENT 3: write a program to print Fibonacci  n series
c=int(input("Enter count:"))
a=-1
b=1
for i in range(0,c):
    c=a+b
    a=b
    b=c
    print(c)
