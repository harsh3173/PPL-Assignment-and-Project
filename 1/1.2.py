#The dice rolling simulator will imitate the experience of rolling a dice. It will generate a random number and the user can play again and again to get a number from the dice until the user decides to quit the program.

import random
while True:
	inp = str(input("Roll dice Y/n: "))
	if inp == 'n' :
		break
	elif inp == 'Y' :
		print(random.randrange(1, 7, 1))
	else:
		print("Invalid input")
