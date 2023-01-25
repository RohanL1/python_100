import random

def print_hand_sign(idx):
	if idx == 0 :
		return """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

	elif idx == 1:
		return """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
	elif idx == 2:
		return """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
try :
    chs=int(input("Welcome to rock, paper and Scissors Game !\n Please choose -> 0 for rock, 1 for paper and 2 for Scissors\n>>"))
    assert chs <= 2 and chs >= 0 
except : 
    print ("Invalid choice") 
    exit(1)
print ("your choice >> \n " + print_hand_sign(chs) )

cm_chs=random.randint(0, 2)
print ("Computer chose >> \n " + print_hand_sign(cm_chs))
print("Result >> ")
if chs == cm_chs:
	print("DRAW")
elif  (chs==0 and cm_chs==2 ) or ( chs > cm_chs) : 
	print("You WIN")
else :
	print("You Lose")
