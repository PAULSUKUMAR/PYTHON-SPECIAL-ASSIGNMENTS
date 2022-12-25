#ASSIGNMENT 1: write a program to print given number is palindrome or not?
n=int(input())
t=n
s=0
while(n!=0):
    r=n%10
    s=(s*10)+r
    n=n//10
if(t==s):
    print("Palindrome")
else:
    print("Not a palindrome")
