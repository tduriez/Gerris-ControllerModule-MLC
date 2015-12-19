lastFF = 0.6
lastFF2 = 0.1
lastDrag = 0.1

def ffForce(forcesList,locList):
	global lastFF
	global lastFF2
	global lastDrag
	if len(forcesList) > 0:
		force = forcesList[0]
#		print str(lastFF)
#		print str(lastDrag)
		drag = force.data.pf[0]*force.data.pf[0] + force.data.pf[1]*force.data.pf[1]
		if drag != lastDrag:
			ff = lastFF - 0.01 * (drag - lastDrag) / (lastFF - lastFF2)
			lastFF2 = lastFF
			lastFF = ff
			lastDrag = drag 
#		print str(ff)
		return lastFF
	return 1

def ffpos(forcesList,locList):
	if len(locList) > 0:
		step1 = locList[0]
		varU = step1.data.varMap["U"]
		suma = 0
		for pos in varU:
			suma += pos[1]
		return suma
	return 1

def myfunc(f,l):
	return 2

def bobo(f,l):
	return 0.6;
