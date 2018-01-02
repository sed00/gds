# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.
name = input("Please provide your name")
age = int(input("Please provide your age"))
if (18 <= age < 31):
	print("welcome to the holiday!")
else:
	print("Sorry, you can't go into the holiday")
