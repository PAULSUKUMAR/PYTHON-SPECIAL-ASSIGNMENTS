#ASSIGNMENT-16:Write a program to print difference between maximum and minimum number from the given list.
n=int(input())
l=list(map(int,input().split()))
min=l[0]
max=l[0]
for i in range(1,n):
    if l[i]<min:
        min=l[i]
    if l[i]>max:
        max=l[i]
print(max-min)
