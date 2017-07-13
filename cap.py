def capacity(K, weights):
	weights = sorted(weights, reverse = True)
	def solve(K, i):
		print("Solve({0}, {1})".format(K, i))
		if K == 0:
			return []
		while i < len(weights) and weights[i] > K:
			i += 1
		if i == len(weights):
			return None
		subK = K - weights[i]
		subI = i + 1
		subsolution = solve(K, subI)
		if subsolution is not None:
			subsolution.append(weights[i])
			return subsolution
		subsolution = solve(K, subI)
		if subsolution is not None:
			return subsolution
		return None
	return solve(K, 0)
print(capacity(2000, [x**2 for x in range(100)]))
