print("Take this quiz to learn which Spongebob character you are!")
krabs = 0
sponge = 0
pat = 0
squid = 0
print("1. What is the best way to spend your day?")
print("A. Cashing in at the casino")
print("B. Hanging with the squad")
print("C. Observing the fine arts")
print("D. Working your favorite job")
answer = input().upper()
if answer == "A":
	krabs = krabs + 1
elif answer == "B":
	pat = pat + 1
elif answer == "C":
	squid = squid + 1
elif answer == "D":
	sponge = sponge + 1
else:
	print("No response recorded")
print("2. What is your favorite snack?")
print("A. Krabby Patty")
print("B. Chocolate Mousse")
print("C. Ketchup Packets")
print("D. Sand")
answer = input().upper()
if answer == "C":
	krabs = krabs + 1
elif answer == "D":
	pat = pat + 1
elif answer == "B":
	squid = squid + 1
elif answer == "A":
	sponge = sponge + 1
else:
	print("No response recorded")
print("3. What is your favorite instrument?")
print("A. Violin")
print("B. Mayonaise")
print("C. Clarinet")
print("D. Ukelele")
answer = input().upper()
if answer == "A":
	krabs = krabs + 1
elif answer == "B":
	pat = pat + 1
elif answer == "C":
	squid = squid + 1
elif answer == "D":
	sponge = sponge + 1
else:
	print("No response recorded")
print("4. Who is your favorite person?")
print("A. Myself, obviously")
print("B. My best friend")
print("C. My grandma")
print("D. My mom")
answer = input().upper()
if answer == "D":
	krabs = krabs + 1
elif answer == "B":
	pat = pat + 1
elif answer == "A":
	squid = squid + 1
elif answer == "C":
	sponge = sponge + 1
else:
	print("No response recorded")
print("5. What is your favorite music?")
print("A. Jazz")
print("B. Techno")
print("C. Pop")
print("D. German Death Reggae")
answer = input().upper()
if answer == "B":
	krabs = krabs + 1
elif answer == "D":
	pat = pat + 1
elif answer == "A":
	squid = squid + 1
elif answer == "C":
	sponge = sponge + 1
else:
	print("No response recorded")
if krabs > pat and krabs > squid and krabs > sponge:
	print("You're the manager of the Krusty Krab, Eugene Krabs!")
elif pat > krabs and pat > squid and pat > sponge:
	print("You're the silly starfish, Patrick Star!")
elif squid > krabs and squid > pat and squid > sponge:
	print("You're the cynical squid, Squidward Tentacles!")
elif sponge > krabs and sponge > pat and sponge > squid:
	print("You're the bubbly main character, Spongebob Squarepants!")
else:
	print("Your results were inconclusive")
