fp = open("/home/vampy/data/ints.txt", "r")
writer = open("/home/vampy/data/intsOut.txt", "w")
islandNum = 0
islands = []
line = fp.readline().strip()
for lineNum in range(int(line)):
	nums = fp.readline().split()
	for i in range(1, 16):
		if nums[i] > nums[i-1]:
			islandNum += 1
	writer.write(str(lineNum + 1) + " " + str(islandNum) + "\n")
	islandNum = 0
