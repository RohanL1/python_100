print("welcome to pizza shop")

#print("Bill :") {'s':15, 'm':20, 'l':25}.[input("size ? S/M/L")] + {'y': , 'n': }.[input("pap ? y/n")] 


sz={'s':15, 'm':20, 'l':25}[str(input("size ? S/M/L > ").lower())]
pap={'y': {15: 2, 20: 3,25:3 }[sz], 'n': 0 }[str(input("pap ? y/n").lower())]
chz=1 if input("extra cheese ? y/n").lower() == 'y' else 0
print("total : " + str(sz+pap+chz))




print("total : " + str( int(1 if input("extra cheese ? y/n").lower() == 'y' else 0 ) + {'y': {15: 2, 20: 3,25:3 }[sz], 'n': 0 }[str(input("pap ? y/n").lower())] + {'s':15, 'm':20, 'l':25}[str(input("size ? S/M/L > ").lower())] ))
#print(str(sz) + " " + str(pap) + " "+ str(chz) )
