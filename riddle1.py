import numpy as np
import utility


# counts the number of red hats and checks whether to ouput red or blue
def countHats(agent,agents):
	numberRedHats=0
	for a in agents[:agent.id-1]:
		if(a.colourHat=='red'):
			numberRedHats += 1
	if numberRedHats % 2 == 0:
		return 'red'
	else:
		return 'blue'


def announcementLoop(agents,model,n,hats):
	counter = 0
	commonKnowledge=[]
	for agent in reversed(agents):
		# only first agent says red or blue to indicate odd or even
		if(agent.id == n):
			print("Agent",agent.id,"announces:")
			number = countHats(agent,agents) # decide if the amount of red hats in front is even or odd
			print('"',number,'"')
			commonKnowledge.append(number) # the number of red hats is added as common knowledge
			updateKripke(model,agent,commonKnowledge,counter)
		else:
			color=deduceHatColour(agent,model,counter)
			print("Agent",agent.id,"announces:")
			print('"',color,'"')
			commonKnowledge.append(color)
			updateKripke(model,agent,commonKnowledge,counter)
		counter +=1
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
			utility.printGraph(model,hats,counter,1)
	return commonKnowledge


# update the model for each agent afer the announcements			
def updateKripke(m,a,commonKnowledge, counter):
	for agent,worlds in m.items():
		if(agent<a.id): #only update the knowledge of the agents in front of the agent that just spoke
			toRemove=[]
			for w in worlds:
				worldSubset=w[1:len(w)] # remove the hat of the tallest player, this is not important
				if(counter == 0): # the first common knowledge is the number of even and odd hats
					if(commonKnowledge[counter]=='red'): # even number
						if(worldSubset.count('red') %2 != 0): # remove subworlds with an odd number of red hats
							toRemove.append(w)
					else: # odd number
						if(worldSubset.count('red') %2 == 0): # remove subworlds with an even number of red hats
							m[agent].remove(w)
				else:
					if(worldSubset[counter-1]!=commonKnowledge[counter]):
						toRemove.append(w)
			for i in toRemove: # remove the list of worlds from the dictionary
				m[agent].remove(i)
				
# deduces the hat colour of an agent
def deduceHatColour(a,m,counter):
	worlds=m[a.id] # copy the worlds of a given agent
	knowsHat=0
	for w in range(0,len(worlds)):
		for nextWorld in range(1,len(worlds)):
			if worlds[w][counter]==worlds[nextWorld][counter] : # compare if the element in the position of the agent is the same for all worlds
				color=worlds[w][counter]
				knowsHat=1
	if knowsHat == 1:
		return color

# check if at most one mistake has been commited
def checkRiddle(c,h):
	h.reverse()
	numberOfMistakes=np.sum(c != h) # count number of dissimilar item
	if numberOfMistakes == 0 :
		print("Wow you are a highly intelligence specie, you will not be eaten!")
	elif numberOfMistakes == 1 :
		print("You are lucky, you made only one mistake so you will not be eaten!")
	else:
		print("Gnam gnam you all will be our dinner!!")


# runs Riddle 1		
def runRiddle1(a,number_prisoners,h):
	m=utility.createAgentKnowledge(a,number_prisoners,h,['blue','red']) # creates the initial kripke model
	c=announcementLoop(a,m,number_prisoners,h) # go in the announcement loop 
	checkRiddle(c,h)
	
