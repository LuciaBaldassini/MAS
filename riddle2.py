# this script implements the second riddle

import utility

# Defines a map from hat color to numbers
hatsCode = {
'yellow': 0, 
'blue': 1,
'red':2
}

# defines an initial tally
INITIAL_NUMBER=30

	
def calculateCheckSum(id,h):
	checkSum=0
	subArray=h[:id-1]
	for hats in subArray:
		if hats in hatsCode:
			checkSum += hatsCode[hats] # calculate the checkSum of the hats in the row in front of each agent
	return checkSum

# returns the color and the associated modulo
def calculateHatColor(checkSum):
	modulo=checkSum%3
	if modulo in hatsCode.values():
		guess = [key for key, value in hatsCode.items() if value == modulo]
		return guess,modulo

def announcementLoop(agents,model,n,hats):
	runningTally=INITIAL_NUMBER
	commonKnowledge=[]
	counter=0
	for agent in reversed(agents):
		# the tallest agent performs the check sum and the modulo division, announces it and the Kripke model is updated
		if agent.id==n:
			s=calculateCheckSum(agent.id,hats)
			c,m=calculateHatColor(s)
			commonKnowledge.append(m)
			runningTally += m  # subtract the modulo from the runningTally
			print("Agent", agent.id, "announces:")
			print(c)
			c, modulo = updateKripkeModel(model, agent, hats, runningTally,c,counter)
		# with the updated Kripke model, the agent next in line make the anouncement and the model is updated again
		else:
			print("Agent", agent.id, "announces:")
			print(c)
			commonKnowledge.append(modulo)
			runningTally -= commonKnowledge[counter]
			if agent.id!=1:
				c,modulo=updateKripkeModel(model, agent, hats, runningTally,c,counter)
		counter += 1
		# ask to optionally draw the Kripke model
		if agent.id!=1:
			while True:
				updatedkripkeChoice= str(input("Would you like to inspect the updated Kripke model (a nice fancy graph will be saved in the same folder as this programme)? [yes/no] \n"))
				if (updatedkripkeChoice != "yes" and updatedkripkeChoice != "no"):
					print("Please enter either yes or no.")
					continue
				else:
					break
			if(updatedkripkeChoice=="yes"):
				utility.printGraph(model,hats,counter)
	return commonKnowledge

# Updates the Kripke model
def updateKripkeModel(m,a,hats, runningTally,previousAnnouncement,counter):
	toRemove = []
	# calculate checksum of the agent next in line
	s = calculateCheckSum(a.id-1, hats)
	# performs modulo division to find the hat color
	c, modulo = calculateHatColor(runningTally - s)
	# the agent next in line has the following worlds removed:
	for worlds in m[a.id-1]:
		if not worlds[counter+1] in c: # the ones in which the agent wears a hat color different from the one deduced
			toRemove.append(worlds)
		if counter!=0:
			if not worlds[counter] in previousAnnouncement and not worlds in toRemove: # the ones in which the previous agent is wearing a different hat (from agent 3 onward)
				toRemove.append(worlds)
	# remove the list of worlds from the dictionary
	for i in toRemove:
		m[a.id-1].remove(i)
	return c,modulo

# function that checks if the riddle was solved and outputs a friendly message.
def calculateTotalWin(hatColors,hats):
	totalWin=0
	hatColors.reverse()
	for h in range(0,len(hats)):
		if hatsCode[hats[h]] == hatColors[h]:
			totalWin += 10000
	print('Congratulations! You won in total',totalWin,'€!')

# runs riddle2
def runRiddle2(a,number_prisoners,h):
	m=utility.createAgentKnowledge(a,number_prisoners,h,['red','blue','yellow'])
	c=announcementLoop(a,m,number_prisoners,h)
	calculateTotalWin(c,h)
