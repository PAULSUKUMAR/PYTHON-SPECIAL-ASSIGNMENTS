#ASSIGNMENT 11:write a program to print sum of n prime numbers
n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        sum=sum+i
print(sum)
