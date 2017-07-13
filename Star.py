import turtle as t
def star(n, k, size):
	angle = k*360/n
	for i in range(n):
		t.forward(size)
		t.right(angle)

