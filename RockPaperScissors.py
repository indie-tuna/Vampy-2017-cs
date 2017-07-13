import random as r
print("Lets play rock paper scissors!")
print("(1)Rock...")
print("(2)Paper...")
print("(3)Scissors...")
c = input("Shoot!")
cc = r.randint(1,3)
if c == "1":
	if cc == 1:
		print("Rock and rock, tie!")
	elif cc == 2:
		print("Paper covers rock, you lose!")
	else:
		print("Rock beats scissors, you win!")
elif c == "2":
	if cc == 1:
		print("Paper covers rock, you win!")
	elif cc == 2:
		print("Paper and paper, tie!")
	else:
		print("Scissors cut paper, you lose!")
elif c == "3":
	if cc == 1:
		print("Rock beats scissors, you lose!")
	elif cc == 2:
		print("Scissors cut paper, you win!")
	else:
		print("Scissors and scissors, tie!")
else: 
	print("No viable responses")
