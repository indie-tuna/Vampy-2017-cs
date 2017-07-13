n = int(input("N: "))
k = int(input("K: "))
answer = 1
for i in range(k):
	answer *= n
print(answer)
