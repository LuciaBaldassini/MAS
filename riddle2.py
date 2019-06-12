def calculateCheckSum(agent,h):
	checkSum=0
	subArray=h[:agent.size-1]
	for hats in subArray:
		if(hats == 'yellow'):
			checkSum += 0
		elif(hats=='blue'):
			checkSum += 1
		elif(hats=='red'):
			checkSum += 2
	print(checkSum)

def runRiddle2(a,number_prisoners,h):
	for agent in reversed(a):
		calculateCheckSum(agent,h)
