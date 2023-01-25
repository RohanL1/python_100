import random

def random_uniq(match_list,lmt):
	# print(match_list,lmt)
	tmp=random.randint(0,lmt)
	if tmp not in match_list:
		return tmp
	else :
		return random_uniq(match_list,lmt)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]
total_ln=nr_letters + nr_symbols + nr_numbers

for i in range(0, total_ln):
    password.append(random.choice(letters))
    #print(password)

# print(password)
temp_chs=[]
for i in range(0, nr_symbols):
    tmp=random_uniq(temp_chs,total_ln-1)
    temp_chs.append(tmp)
    password[tmp]=random.choice(symbols)

# print(temp_chs)
# print(password)
for i in range(0, nr_numbers):
    tmp=random_uniq(temp_chs,total_ln-1)
    temp_chs.append(tmp)
    password[tmp]=random.choice(numbers)


print(password)
