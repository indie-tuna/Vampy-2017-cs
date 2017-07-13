f = open("Grades.txt", "w")
name = input("What is your name?")
print("Type '-1' to stop")
grade = 0
test_count = 0
test_sum = 0
while grade != -1:
	grade = float(input("Enter your test Grades:"))
	test_count = test_count + 1
	test_sum = test_sum + grade
print(name+"\n==========\n Average: "+str(test_sum/test_count))
