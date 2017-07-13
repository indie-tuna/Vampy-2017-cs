def capacity(K, w):
	w.sort(reverse = True)
	return _capacity(K, w)
def _capacity(K, w):
	cut = 0
	while w[cut] > K:
		cut += 1
	w = w[cut:]
	sub =  _capacity(K-w[0], w[1:])
	if sub is None:
		sub = _capacity(K, w{1:])
		if sub is None:
			return None
		else:
			return sub
	else:
		sub.append(w[0])
	return sub
