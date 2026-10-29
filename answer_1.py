print("small pizza:Rs.150 medium pizza Rs.200 large pizza:Rs.250")
print("Pepporoni for small pizza: Rs.20\n Pepporoni for medium or large pizza: Rs.30\n Extra cheese for any size pizza Rs.10")

total=0
size=input("Choose size (S,M,L):")
if size=="S":
    Pepperoni4S=input("Do you want Pepperoni (y/n) : ")
    if Pepperoni4S=="y":
        total=150+20
    else:
        print("enter Valid input")
    cheese=input("Do yo want Extra cheese (Y/N) : ")
    if cheese=="Y":
        total += 10
    else:
        print("enter Valid input")
    print("Total Amount to Pay : ", total)
elif size=="M":
    Pepperoni4M=input("Do you want Pepperoni (y/n) : ")
    if Pepperoni4M=="y":
        total=200+30
    else:
        print("enter Valid input")
    cheese=input("Do yo want Extra cheese (Y/N) : ")
    if cheese=="Y":
        total+=10
    else:
        print("enter Valid input")
    print("Total Amount to Pay : ", total)
elif size=="L":
    Pepperoni4M=input("Do you want Pepperoni (y/n) : ")
    if Pepperoni4M=="y":
        total=250+30
    else:
        print("enter Valid input")
    cheese=input("Do yo want Extra cheese (Y/N) : ")
    if cheese=="Y":
        total+=10
    else:
        print("enter Valid input")
    print("Total Amount to Pay : ", total)



