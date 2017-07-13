import random
def ask(num, scores, question, answers):
	"""
	example, ask(2, scores, "What is your favorite color?",
                     [["Red", "patrick"], ["Blue", "squidward"], ["Yellow", "spongebob"]])
	"""
	random.shuffle(answers)
	letters = ["A", "B", "C", "D", "E"]

	print("{0}. {1}".format(num, question))
	for i in range(len(answers)):
		print("{0}. {1}".format(letters[i], answers[i][0]))
	
	answer = input().upper()
	index = -1
	for i in range(len(letters)):
		if answer == letters[i]:
			index = i
	
	if index == -1:
		print("No response recorded")
	else:
		scores[answers[index][1]] = scores.get(answers[index][1], 0) + answers[index][2]

questions = [
             "What is the best way to spend your day?",
             "What is your favorite snack?"
            ]

answers = [
           [ # What is the best way to spend your day?
            ["Cashing in at the casino", "krabs", 1.0],
            ["Hanging with the squad", "patrick", 0.3],
            ["Observing the fine arts", "squidward", 0.9],
            ["Working your favorite job", "spongebob", 1.0]
           ],
           [ # What is your favorite snack?
            ["Ketchup Packets", "krabs", 0.8],
            ["Sand", "patrick", 0.6],
            ["Chocolate Mousse", "squidward", 0.4],
            ["Krabby Patty", "spongebob", 1.0]
           ]
          ]

scores = {}
for i in range(len(questions)):
	ask(i+1, scores, questions[i], answers[i])

# todo check scores
print(scores)
