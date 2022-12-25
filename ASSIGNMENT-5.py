#ASSIGNMENT 5: write a program to print given number is prime or not
n=int(input("Enter n:"))
c=0
for i in range(2,n):
    if(n%i==0):
        c=c+1
if(c==0):
    print("Prime")
else:
    print("Not a prime")
