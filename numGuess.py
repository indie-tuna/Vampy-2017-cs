lower = 1
upper = 0
guess = 1
ans = ""
while ans != "yes":
	ans = input("Is "+ str(guess) +" your number/ is your number more or less? (yes/more/less)").lower()
	if ans == "more":
		if upper == 0:
			guess *= 2
		else:
			lower = guess
			guess = int((lower + upper)/2)
	elif ans == "less":
		if upper == 0:
			lower = int(guess / 2)
		upper = guess
		guess = int((lower + upper)/2)
print("I found your number!")

