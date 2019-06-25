# This script implements Riddle 1 with either Strategy 1 or Strategy 2

import numpy as np
import utility


# Counts the number of red hats
def countHats(agent,agents):
	numberRedHats=0
	for a in agents[:agent.id-1]:
		if(a.colourHat=='red'):
			numberRedHats += 1
	return numberRedHats

# Announcement loop for Strategy 2
def announcementLoopStrategy2(agents,model,n,hats):
	counter=0
	commonKnowledge=[]
	for agent in reversed(agents):
		# The tallest agent announces either blue or pass (see Strategy)
		if agent.id==n:
			print("Agent", agent.id, "announces:")
			number=countHats(agent,agents)
			if number==(n-1):
				print('blue')
				commonKnowledge.append('blue')
			else:
				print('pass')
				commonKnowledge.append('pass')
			updateKripkeStrategy2(model,commonKnowledge,agent,counter,n)
		# The other agents deduce their hat colour based on the updated Kripke model
		else:
			color=deduceHatColour(agent,model,counter)
			print("Agent", agent.id, "announces:")
			print(color)
			commonKnowledge.append(color)
			updateKripkeStrategy2(model,commonKnowledge, agent, counter,n)
		counter += 1
		if agent.id!=1:
			while True:
				updatedkripkeChoice = str(input("Would you like to inspect the updated Kripke model (i.e. a nice fancy graph will be saved in the same folder as this programme)? [yes/no] \n"))
				if (updatedkripkeChoice != "yes" and updatedkripkeChoice != "no"):
					print("Please enter either yes or no.")
					continue
				else:
					break
			if (updatedkripkeChoice == "yes"):
				utility.printGraph(model, hats, counter)
	return commonKnowledge

# Updates the Kripke model
def updateKripkeStrategy2(m,commonKnowledge,a,counter,n):
	for agent,worlds in m.items():
		# Update the worlds of the agent(s) in front of the one that just spoke
		if agent<a.id:
			toRemove=[]
			for w in worlds:
				worldSubset = w[1:len(w)]
				if counter==0: #First announcement
					if commonKnowledge[counter] == 'blue':
						if 'blue' in worldSubset == True: #Remove all worlds that contain a blue hat
							toRemove.append(w)
					else: # Case in which agent 1 passed
						if worldSubset.count('red') == n - 1:  # Remove the worlds that contains all red hats
							toRemove.append(w)
				else: # From second agent onwards
					if 'blue' in commonKnowledge or 'red' in commonKnowledge: #Say RED if someone made a guess
						if worldSubset[counter] == 'blue':
							toRemove.append(w)
					elif commonKnowledge.count('pass') == len(commonKnowledge): # Say BLUE if all the agents who declared before him passed and
						if a.id!=1 and worldSubset.count('red') == len(worldSubset): # he sees nothing but RED hats in front of him: this holds for all agents except agent 1:
							if worldSubset[counter]=='red':
								toRemove.append(w)
						else: # Agent 1
							if worldSubset[counter]=='red':
								toRemove.append(w)
			for i in toRemove: # Remove the list of worlds from the dictionary
				m[agent].remove(i)




def announcementLoopStrategy1(agents, model, n, hats):
	counter = 0
	commonKnowledge=[]
	for agent in reversed(agents):
		# The tallest agent says red or blue to indicate odd or even
		if(agent.id == n):
			print("Agent",agent.id,"announces:")
			number = countHats(agent,agents) # Decide if the amount of red hats in front is even or odd
			if  number % 2 == 0:
				print('red')
				commonKnowledge.append('red')
			else:
				print('blue')
				commonKnowledge.append('blue')
			updateKripkeStrategy1(model, agent, commonKnowledge, counter)
		# The other agents deduce the hat colours based on the updated Kripke model
		else:
			color=deduceHatColour(agent,model,counter)
			print("Agent",agent.id,"announces:")
			print(color)
			commonKnowledge.append(color)
			updateKripkeStrategy1(model, agent, commonKnowledge, counter)
		counter +=1
		# Ask the user whether to print the graph or not
		if agent.id!=1:
			while True:
				updatedkripkeChoice= str(input("Would you like to inspect the updated Kripke model (i.e a nice fancy graph will be saved in the same folder as this programme)? [yes/no] \n"))
				if (updatedkripkeChoice != "yes" and updatedkripkeChoice != "no"):
					print("Please enter either yes or no.")
					continue
				else:
					break
			if(updatedkripkeChoice=="yes"):
				utility.printGraph(model,hats,counter)
	return commonKnowledge


# Update the model for each agent after the announcements
def updateKripkeStrategy1(m, a, commonKnowledge, counter):
	for agent,worlds in m.items():
		if agent<a.id: #Only update the knowledge of the agents in front of the agent that just spoke
			toRemove=[]
			for w in worlds:
				worldSubset=w[1:len(w)]# Remove the hat of the tallest player, this is not important
				if counter == 0: # The first common knowledge is the number of even and odd hats
					if commonKnowledge[0]=='red': # even number
						if worldSubset.count('red') %2 != 0: # Remove subworlds with an odd number of red hats
							toRemove.append(w)
					else: # odd number
						if worldSubset.count('red') %2 == 0: # Remove subworlds with an even number of red hats
							m[agent].remove(w)
				else:
					if worldSubset[counter-1]!=commonKnowledge[counter]:
						toRemove.append(w)
					if commonKnowledge[0]=='red' and w not in toRemove: # Even number
						if worldSubset.count('red') %2 != 0: # Remove subworlds with an odd number of red hats
							toRemove.append(w)
					elif commonKnowledge[0]=='blue' and w not in toRemove: # odd number
						if worldSubset.count('red') %2 == 0: # Remove subworlds with an even number of red hats
							m[agent].remove(w)
			for i in toRemove: # Remove the list of worlds from the dictionary
				m[agent].remove(i)
				
# Deduces the hat colour of an agent
def deduceHatColour(a,m,counter):
	worlds=m[a.id] # Copy the worlds of a given agent
	knowsHat=1
	for w in range(0,len(worlds)):
		for nextWorld in range(1,len(worlds)):
			if worlds[w][counter]!=worlds[nextWorld][counter] : # Compare if the element at the position of the agent is the same for all worlds
				knowsHat=0
				break
			else:
				continue
			break

	if knowsHat == 1:
		return worlds[w][counter]
	else:
		return 'pass'

# Check if at most one mistake has been committed
def checkRiddle(c,h,strategy):
	h.reverse()
	if strategy==1: # check riddle strategy1
		numberOfMistakes=np.sum(c != h) # count number of dissimilar item
		if numberOfMistakes == 0 :
			print("Wow! You are a highly intelligence species! You will not be eaten!")
		elif numberOfMistakes == 1 :
			print("You are lucky, you made only one mistake so you will not be eaten!")
		else:
			print("Yum yum! You will all be our dinner!!")
	else: # check riddle strategy 2
		mistake=0
		counter = 0
		while counter < len(c)-1:
			if c[counter] != h[counter] and c[counter]!= 'pass':
				mistake=1
				break
			else:
				counter += 1
				continue
			break
		if mistake == 0:
			print("You are intelligent enough, you will be spared!")
		else:
			print("Yum yum! You will all be our dinner!!")



# runs Riddle 1 with either strategy 1 or 2
def runRiddle1(a,number_prisoners,h,strategy):
	m=utility.createAgentKnowledge(a,number_prisoners,h,['blue','red']) # creates the initial kripke model
	if(strategy==1):
		c=announcementLoopStrategy1(a, m, number_prisoners, h) # go in the announcement loop
		checkRiddle(c,h,1)
	else:
		c=announcementLoopStrategy2(a,m,number_prisoners,h) # go in the announcement loop
		checkRiddle(c, h, 2)
