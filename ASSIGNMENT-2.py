#ASSIGNMENT 2: write a program to print given year is leap year or not
y=int(input("Enter year:"))
if((y%4==0)and((y%400==0)or(y%100!=0))):
    print("Leap year")
else:
    print("Not a leap year")
