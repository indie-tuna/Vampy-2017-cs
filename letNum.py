printStr = ""
letters = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
K = int(input("meme"))
for i in range(len(letters)):
	for x in range(K):
		printStr += letters[x]
	print(printStr)
	printStr = ""
		
