#ASSIGNMENT 14:write a program to print previous happy number of the given number?
def happy(n):
    s=0
    while n!=0:
        r=n%10
        s=s+r*r
        n=n//10
    return s
a=int(input())
while a!=0:
    b=a
    while b>9:
        b=happy(b)
    if b==1 or b==7:
        print(a)
        break
    a=a-1
