friends = ["Bill","Tom","Joj","Jaf","Ggg"]
g = input("Find who?").title()
for person in friends:
	if person == g:
		print("Present")
		quit()
print("Absent")
