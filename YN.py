answer = input("Am I an object or a place? (Y/N): ").upper()
if answer == "Y":
	answer = input("Am I bigger than a computer? (Y/N): ").upper()
	if answer == "Y":
		answer = input("Am I a building?").upper()
		if answer == "Y":
			answer = input("Am I a bowling alley? ").upper()
			if answer == "Y":
				print("I am a bowling alley. ")
			else:
				print("I am a salon. ")
		else:
			answer = input("Am I New York? ").upper()
			if answer == "Y":
				print("I am New York. ")
			else:
				print("I am an umbrella. ")
	else:
		answer = input("Am I consumable? ").upper()
		if answer == "Y":
			answer = input("Am I pizza? ").upper()
			if answer == "Y":
				print("I am pizza. ")
			else:
				print("I am soap. ")
		else:
			answer = input("Am I a hat? ").upper()
			if answer == "Y":
				print("I am a hat. ")
			else:
				print("I am a computer. ")
else:
	answer = input("Am I human? (Y/N): ").upper()
	if answer == "Y":
		answer = input("Am I fictional? ").upper()
		if answer == "Y":
			answer = input("Am I Santa Claus").upper()
			if answer == "Y":
				print("I am Santa Claus. ")
			else:
				print("I am James bond. ")
		else:
			answer = input("Am I Michael Jackson? ").upper()
			if answer == "Y":
				print("I am Michael Jackson. ")
			else:
				print("I am Britney Spears. ")
	else:
		answer = input("Can I fit in a coffee mug? ").upper()
		if answer == "Y":
			answer = input("Am I a rat? ").upper()
			if answer == "Y":
				print("I am a rat. ")
			else:
				print("I am a frog. ")
		else:
			answer = input("Am I a chicken? ").upper()
			if answer == "Y":
				print("I am a chicken. ")
			else: 
				print("I am Dracula. ")
