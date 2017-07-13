id = 0
tops = ["Cross Country", "Solid", "Stripes", "VAMPY", "Tie-dye"]
bottoms = ["Khakis", "Blue shorts", "Red shorts", "Running Shorts"]
shoes = ["Flip-flops", "Running Shoes"]
headgear = ["Red bandana", "Black bandana", "Yellow bandana", "Dark blue bandana"]
socks = ["Black Socks", "Dress socks", "White socks", "Athletic socks"]
pattern = "#{0}: Top = {1}, Bottom = {2}, Shoes = {3}, Headgear = {4}, Socks = {5}"
for top in tops:
	for bottom in bottoms:
		for kicks in shoes:
			for item in headgear:
				for pair in socks:
					id += 1
					print(pattern.format(id, top, bottom, kicks, item, pair))

