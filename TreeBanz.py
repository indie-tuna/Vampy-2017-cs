def tree(val):
	return [None, val, None]
def data(node, val = None):
	if node is None:
		return None
	elif val is None:
		return node[1]
	else:
		node[1] = val

def yes(node, child = None):
	if node is None:
		return None
	elif child is None:
		return node[0]
	else:
		node[0] = child
def no(node, child = None):
	if node is None:
		return None
	elif child is None:
		return node[2]
	else:
		node[2] = child
root = tree("Am I an object or a place? (Y/N): ")
yes(root, tree("Am I bigger than a PC? (Y/N): "))
no(root, tree("Am I human? (Y/N): "))

yes(yes(root), tree("Am I a building? (Y/N): "))
no(yes(root), tree("Am I consumed as you use me? (Y/N): "))
yes(no(root), tree("Am I fictional? (Y/N): "))
no(no(root), tree("Can you fit me in a coffe mug (Y/N): "))

yes(yes(yes(root), tree("Am I a salon?")))
no(yes(yes(root), tree("Am I New York?")))
yes(no(yes(root), tree("Am I pizza?")))
no(no(yes(root), tree("Am I a hat?")))

yes(yes(no(root), tree("Am I Santa Claus?")))
no(yes(no(root), tree("Am I MJ?")))
yes(no(no(root), tree("Am I a rat?")))
no(no(no(root), tree("Am I Dracula?")))

yes(yes(yes(yes(root), tree("Salon!"))))
no(yes(yes(yes(root), tree("New York!"))))
yes(no(yes(yes(root), tree("Pizza!"))))
no(no(yes(yes(root), tree("A hat!"))))

yes(yes(no(yes(root), tree("Santa Claus!"))))
no(yes(no(yes(root), tree("MJ!"))))
yes(no(no(yes(root), tree("A rat!"))))
no(no(no(yes(root), tree("Dracula!"))))

yes(yes(yes(no(root), tree("Bowling alley!"))))
no(yes(yes(no(root), tree("Umbrella!"))))
yes(no(yes(no(root), tree("Bar of soap!"))))
no(no(no(no(root), tree("Computer!"))))

yes(yes(no(no(root), tree("James Bond!"))))
no(yes(no(no(root), tree("Britney Spears!"))))
yes(no(no(no(root), tree("Frog!"))))
no(no(no(no(root), tree("Chicken!"))))

tracker = root
while "?" in data(tracker):
	answer = input(data(tracker))
	if answer == "Y":
		tracker = yes(tracker)
	else:
		tracker = no(tracker)
print(data(tracker))


