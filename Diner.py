order = 1
scoopCost = 0.0
extraCost = 0.0
flavScoop = {}
toppings = []
print("Welcome to John Doe's famous creamery!")
print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~")
print("Classic Flavors:")
print("One scoop: 2/ Two scoop: 3.5")
print("Vanilla/ Chocolate/ Strawberry/ Coffee/ Mint")
print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~")
print("Specialty Flavors:")
print("One scoop: 2.4/ Two scoop: 4.2")
print("FACP/ Caramel/ Lemon Scone/ Beetlejuice")
print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~")
print("Cone Selection:")
print("Sugar: 50/ Waffle: 75")
print("+ Chocolate : 50/ + ChocSprinkles: 75")
print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~")
print("Topping Selection (25 each):")
print("Sprinkles/ Cherries/ Chocolate Syrup/ Strawberry Syrup")
print("M&M's/ Oreo/ Salt/ Toffee")
c1 = input("What is your first flavor?").lower()
c2 = int(input("How many scoops?"))
flavScoop[c1] = c2
loop = input("Would you like another flavor?").lower()
while loop not in ["no","n","nope"]:
	loop = input("Would you like another flavor?").lower()
	c1 = input("What is your next flavor?").lower()
	c2 = int(input("How many scoops?"))
	flavScoop[c1] = c2
	loop = input("Would you like another flavor?").lower()
c3 = input("Cone or bowl?").lower()
if c3 == "cone":
	c4 = input("Sugar or waffle?").lower
	if c4 == "sugar":
		extraCost += .50
	else:
		extraCost += .75
	dipped = input("Would you like your cone dipped?")
	if dipped in ["yes","y","sure"]:
		c5 = input("Chocolate or chocolate with sprinkles?").lower
		if c5 == "chocolate":
			extraCost += .50
		else:
			extraCost += .75
loopFrequency = 0
c6 = input("Would you like toppings?").lower
while c6 not in ["no","n","nope"]:
	topping = input("What topping would you like?").lower
	toppings.append(topping)
	extraCost += .25
	c6 = input("Would you like another topping?")
	loopFrequency += 1
for c1 in flavScoop:
	if c1 in ["vanilla" , "chocolate" , "strawberry" , "coffee" , "mint"]:
		if c2 % 2 == 0:
			scoopCost += float(c2) * 1.75
		else:
			scoopCost += float(c2 - 1) * 1.75 + 2.0
	else:
		if c2 % 2 == 0:
			scoopCost += float(c2) * 2.1
		else:
			scoopCost += float(c2 - 1) * 2.1 + 2.4
for c1 in flavScoop:
	print("You ordered "+ str(c2) +" scoop(s) of "+ c1 +".")
print("Your ice cream came with "+ str(loopFrequency) +" topping(s).")
for i in range(loopFrequency):
	print("You asked for extra "+ str(toppings[i]) +".")
print("Your total is: "+ str(extraCost + scoopCost))
	

