#ASSIGNMENT 15:Write a program to print Unique single number for the duplicate list?
n=int(input())
l=list(map(int,input().split()))
for i in l:
    count=0
    for j in l:
        if i==j:
            count=count+1
    if count==1:
        print(i,end=" ")
