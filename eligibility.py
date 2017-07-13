dictInfo = {}
names = []
ps = []
db = []
psNew = []
dbNew = []
eligibility = []
courses = []
cases = input()
	if int(cases) <= 1000:
	for i in range(int(cases)):
		info = input()
		arrayInfo = info.split()
		dictInfo[i] = arrayInfo
		names.append(dictInfo[i][0])
		ps.append(dictInfo[i][1])
		db.append(dictInfo[i][2])
		courses.append(dictInfo[i][3])
	for i in range(int(cases)):
		psArray = ps[i].split("/")
		dbArray = db[i].split("/")
		psNew.append(psArray[0])
		dbNew.append(dbArray[0])
	for i in range(int(cases)):
		if int(psNew[i]) >= 2010 or int(dbNew[i]) >= 1991:
			eligibility.append("eligible")
		elif int(courses[i]) > 40:
			eligibility.append("ineligible")
		else:
			eligibility.append("coach petitions")
	for i in range(int(cases)):
		print(names[i], eligibility[i])
