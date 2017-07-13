import Sorting
filename = "/home/vampy/data/test1"
fp = open(filename, "r")
N = int(fp.readline())
names = []
for i in range(N):
	names.append(fp.readline().strip())
fp.close()
print(names)
Sorting.merge(names)
print(names)
