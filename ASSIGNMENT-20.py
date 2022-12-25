#ASSIGNMENT 20:Write a program to maximum prime number and minimum prime number from the given list.
n=int(input())
plist=[]
l=list(map(int,input().split()))
for i in l:
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=c+1
    if(c==0):
        plist.append(i)
min=plist[0]
max=plist[0]
for i in plist:
    if i<min:
        min=i
    if i>max:
        max=i
print(min)
print(max)
    
