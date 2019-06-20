import utility

hatsCode = {
'yellow': 0, 
'blue': 1,
'red':2
}

INITIAL_NUMBER=30

	
def calculateCheckSum(id,h):
	checkSum=0
	subArray=h[:id-1]
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
			s=calculateCheckSum(agent.id,hats)
			c,m=calculateHatColor(s)
			commonKnowledge.append(m)
			runningTally += m  # subtract the modulo from the runningTally
			print("Agent", agent.id, "announces:")
			print(c)
			c, modulo = updateKripkeModel(model, agent, hats, runningTally,c,counter)
		else:
			print("Agent", agent.id, "announces:")
			print(c)
			commonKnowledge.append(modulo)
			runningTally -= commonKnowledge[counter]
			if agent.id!=1:
				c,modulo=updateKripkeModel(model, agent, hats, runningTally,c,counter)
		counter += 1
		if agent.id!=1:
			while True:
				updatedkripkeChoice= str(input("Would you like to inspect the updated Kripke model? [yes/no] \n"))
				if (updatedkripkeChoice != "yes" and updatedkripkeChoice != "no"):
					print("Please enter either yes or no.")
					continue
				else:
					break
			if(updatedkripkeChoice=="yes"):
				print("The Kripke model after announcement",counter,"is:")
				print(dict(model))
				utility.printGraph(model,hats,counter,2)
	return commonKnowledge

def updateKripkeModel(m,a,hats, runningTally,previousAnnouncement,counter):
	toRemove = []
	s = calculateCheckSum(a.id-1, hats)
	c, modulo = calculateHatColor(runningTally - s)
	for worlds in m[a.id-1]:
		if not worlds[counter+1] in c: # only for agent 2 removes the worlds in which the agent is not wearing the hat with the deduced color
			toRemove.append(worlds)
		if counter!=0:
			if not worlds[counter] in previousAnnouncement and not worlds in toRemove:
				toRemove.append(worlds)

	for i in toRemove:  # remove the list of worlds from the dictionary
		m[a.id-1].remove(i)
	return c,modulo
			
def calculateTotalWin(hatColors,hats):
	totalWin=0
	print(hats)
	hatColors.reverse()
	for h in range(0,len(hats)):
		if hatsCode[hats[h]] == hatColors[h]:
			totalWin += 10000
	print('Congratulations! You won in total',totalWin,'€!')

def runRiddle2(a,number_prisoners,h):
	m=utility.createAgentKnowledge(a,number_prisoners,h,['red','blue','yellow'])
	c=announcementLoop(a,m,number_prisoners,h)
	calculateTotalWin(c,h)
