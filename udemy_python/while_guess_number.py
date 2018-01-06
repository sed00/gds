# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 10
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
count = 1
while guess != answer:
	if (guess == 0):
		break
	if (guess < answer):
		print("Please guess higher")	
	else:
		print("Please guess lower")
	count+=1
	guess = int(input())
else:
	print("You guess it after {} times".format(count))

