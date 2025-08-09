"""n=int(input("enter the integer"))
if n%2==0:
    if 2<=n<=5:
        print("not weired")
    elif 6<=n<=20:
        print("Weired")
    elif n>20:
        print("Not Weired")
else:
    print("Weired")"""
    
year=int(input("enter the year"))
if year%4==0 and year%100!=0 or year%400==0:
    print("its leap year")
else :
    print("not leap year")