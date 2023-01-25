# Initializing string
ini_string = 'abcdebf'
ini_string2 = 'xyze'

# Character to find
c = "b"
# printing initial string and character
print("initial_strings : ", ini_string, " ",
	ini_string2, "\ncharacter_to_find : ", c)

# Using find Method
res1 = ini_string.find(c)
res2 = ini_string2.find(c)

if res1 == -1:
	print("No such character available in string {}".format(
		ini_string))
else:
	print("Character {} in string {} is present at {}".format(
		c, ini_string, str(res1 + 1)))

if res2 == -1:
	print("No such character available in string {}".format(
		ini_string2))
else:
	print("Character {} in string {} is present at {}".format(
		c, ini_string2, str(res2 + 1)))
