#ASSIGNMENT 8:write a program to print leap years upto given range
s = int(input("Enter start year: "))
e = int(input("Enter end year: "))
while s<=e:
     if ((s%400==0) or ((s%4==0) and (s%100!=0))):
         print(s)
     s += 1
