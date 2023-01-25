try :
    while True : 
        try : 
            print( "ODD" if int(input("Enter number to check for odd/even : ")) % 2 > 0 else "EVEN")
        except ValueError : print("enter numbers only !!")
except KeyboardInterrupt :  print("exiting..")  or exit(1)
