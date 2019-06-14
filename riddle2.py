import utility

hatsCode = {
'yellow': 0, 
'blue': 1,
'red':2
}

INITIAL_NUMBER=30

	
def calculateCheckSum(agent,h):
	checkSum=0
	subArray=h[:agent.id-1]
	for hats in subArray:
		if hats in hatsCode:
			checkSum += hatsCode[hats] # calculate the checkSum of the hats in the row in front of each agent
	return checkSum
	
def calculateHatColor(checkSum):
	modulo=checkSum%3
	if modulo in hatsCode.values():
		guess = [key for key, value in hatsCode.items() if value == modulo]
		return guess,modulo # return the color associated with each modulo

def announcementLoop(agents,model,n,hats):
	runningTally=INITIAL_NUMBER
	commonKnowledge=[]
	counter=0
	for agent in reversed(agents):
		if agent.id==n:
			s=calculateCheckSum(agent,hats)
			c,m=calculateHatColor(s)
			commonKnowledge.append(m)
			runningTally -= m  # subtract the modulo from the runningTally
			print("Agent", agent.id, "announces:")
			print('"',c, '"')
		else:
			runningTally -= commonKnowledge[counter] # subtract previousely called color from running tally
			s=calculateCheckSum(agent,hats)
			c,m=calculateHatColor(runningTally-s)
			commonKnowledge.append(m)
			print("Agent", agent.id, "announces:")
			print('"', c, '"')
			counter += 1
	return commonKnowledge
			
def calculateTotalWin(hatColors,hats,n):
	totalWin=0
	for h in range(0,len(hats)):
		if hatsCode[hats[h]] == hatColors[h]:
			totalWin += 10000
	print('Congratulations! You won in total',totalWin,'€!')

def runRiddle2(a,number_prisoners,h):
	m=utility.createAgentKnowledge(a,number_prisoners,h,['red','blue','yellow'])
	c=announcementLoop(a,m,number_prisoners,h)
	calculateTotalWin(c,h,number_prisoners)
