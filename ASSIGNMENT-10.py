#ASSIGNMENT 10:write a program to count n prime numbers in the given range
n=int(input("Enter n:"))
count=0
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        count=count+1
print(count)
