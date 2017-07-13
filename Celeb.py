connections = {}
connections["Joj"]     = []
connections["Emily"]   = ["Joj", "Jeph", "Jeff"]
connections["Jeph"]    = ["Joj", "Geoff"]
connections["Jeff"]    = ["Joj", "Judge"]
connections["Geoff"]   = ["Joj", "Jeb"]
connections["Jebb"]    = ["Joj", "Emily"]
connections["Judge"]   = ["Joj", "Judy"]
connections["Jodge"]   = ["Joj", "Jebb", "Stephan", "Judy"]
connections["Judy"]    = ["Joj", "Judge"]
connections["Stephan"] = ["Joj", "Jodge"]

names = ["Emily", "Jeph", "Jeff", "Geoff", "Jebb", "Judge", "Joj", "Jodge", "Judy", "Stephan"]
candidate = names[0]
for i in range(1, len(names)):
	if names[i] in connections[candidate]:
		candidate = names[i]
print("The celebrity is most likely "+ candidate +".")
for name in names:
	if name != candidate and name in connections[candidate]:
		print("The first proposal knows someone, and is false.")
		exit()
	elif name != candidate and candidate not in connections[name]:
		print("The first proposal is unknown by all, and is false.")
		exit()
print("The first proposal is accurate.")
