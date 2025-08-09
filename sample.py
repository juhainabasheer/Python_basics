a=int(input("enter the first number :"))
b=int(input("enter the second number :"))

print("select your choice:")
print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.division")
# choice=int(input("enter the choice - 1,2,3,4 :"))
"""if choice==1:
    print(f"sum of 2 no.s is {a+b}") 
elif choice==2:
    print(f"difference of 2 no.s is{a-b}")
elif choice==3:
    print(f"Multiplication of 2 no.s is {a*b}")
elif choice==4:
    if b!=0:
        print(f"Division of 2 no.s is {a/b} ")
    else:
        print("not valid")
else:
    print("invalid choice") """
"""match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case __:
        print("Invalid input")"""
choice=(input("enter the choice - 1,2,3,4 :"))
match choice:
    case '1' | "+":
        print(a+b)
    case '2' | "-":
        print(a-b)
    case '3'| "*":
        print(a*b)
    case '4'|"/":
        print(a/b)
    case __:
        print("Invalid input")
