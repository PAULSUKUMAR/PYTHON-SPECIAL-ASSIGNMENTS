#Write a program to print square root of the given number.
#If square root is greater than 10,print 'Hello' otherwiseprint 'Hi'
import math 
n=int(input())
SquareRoot=math.sqrt(n)
if(SquareRoot>10):
    print("HELLO")
else:
    print("HI")

