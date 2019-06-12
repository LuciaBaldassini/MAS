import utility

hatsCode = {
'yellow': 0, 
'blue': 1,
'red':2
}

	
def calculateCheckSum(agent,h):
	checkSum=0
	subArray=h[:agent.id-1]
	for hats in subArray:
		if hats in hatsCode:
			checkSum += hatsCode[hats] # calculate the checkSum of the hats in the row in front of each agent
	return checkSum
	
def calculateHatColor(checkSum,commonKnowledge):
	modulo=checkSum%3
	if modulo in hatsCode.values():
		guess = [key for key, value in hatsCode.items() if value == modulo]
	
		return guess # return the color associated with each modulo

def runRiddle2(a,number_prisoners,h):
	commonKnowledge=[]
	m=utility.createAgentKnowledge(a,number_prisoners,h,['red','blue','yellow'])
	for agent in reversed(a):
		s=calculateCheckSum(agent,h)
		#c=calculateHatColor(s,commonKnowledge)
		#commonKnowledge.append(c)
