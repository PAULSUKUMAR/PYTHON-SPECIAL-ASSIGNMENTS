#ASSIGNMENT 9:write a program to print sum of n febnocci  series
n=int(input("Enter n:"))
sum=0
a,b=-1,1
for i in range(0,n):
    c=a+b
    print(c)
    sum=sum+c
    a=b
    b=c
print("Sum=",sum)
