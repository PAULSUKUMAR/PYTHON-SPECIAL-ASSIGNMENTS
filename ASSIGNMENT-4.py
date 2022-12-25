#ASSIGNMENT 4:write a program to find maximum and minimum from the given digit
def func(n):
    l=0
    sm=9  
    while(n):
        r = n% 10;
        l= max(r, l);
        sm= min(r, sm);
        n = n // 10
    print("MAXIMUM:",l)
    print("MINIMUM:",sm)
n=int(input("Enter n:"))
func(n)
