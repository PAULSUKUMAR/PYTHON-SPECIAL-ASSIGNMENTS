#ASSIGNMENT 6:write a program to print given number is happy number or not
n=int(input("Enter n:"))
while(n>9):
    s=0
    while(n>0):
        r=n%10
        s=s+(r*r)
        n=n//10
    n=s
if(s==1 or s==7):
    print("Happy number")
else:
    print("Not a happy number")
