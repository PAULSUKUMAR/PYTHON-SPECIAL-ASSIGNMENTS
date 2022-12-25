#ASSIGNMENT 7:write a program to print given number is perfect or not
n=int(input("Enter n:"))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print("Perfect")
else:
    print("Not a perfect")
