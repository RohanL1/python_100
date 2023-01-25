total=float(input("Welcome to tip calculator.\nWhat was the total bill ? $"))
people_count=int(input("How many ppl ?"))
tip_per=float(input("tip ? 10/12/15 ?"))

print("Each person should pay: ${}".format(str(round((total + (total * (tip_per/100) ))/people_count,2))))
