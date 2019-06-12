import Kripke
import numpy as np
import networkx as nx
from itertools import product
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import graphviz


# counts the number of red hats and checks whether to ouput red or blue
def countHats(agent,agents):
	numberRedHats=0
	for a in agents[:agent.size-1]:
		if(a.colourHat=='red'):
			numberRedHats += 1
	if numberRedHats % 2 == 0:
		return 'red'
	else:
		return 'blue'
		
# creates the knowledge of each agent at the beginning of the riddle (before any announcements)		
def createAgentKnowledge(agents,n,hats):
	allWorlds=list(product(['blue','red'],repeat = n)) # creates all possible worlds
	kripke = Kripke.Kripke(agents,allWorlds,hats) # define a new Kripke model
	model=kripke.createKripkeModel()
	while True:
		kripkeChoice= str(input("Would you like to inspect the initial Kripke model? [yes/no] \n"))
		if (kripkeChoice != "yes" and kripkeChoice != "no"):
			print("Please enter either yes or no.")
			continue
		else:
			break
	if(kripkeChoice=="yes"):
		print("The Kripke model before any announcement is made is:")
		print(dict(model))
		printGraph(model,hats,0)
	return model

def announcementLoop(agents,model,n,hats):
	counter = 0
	commonKnowledge=[]
	for agent in reversed(agents):	
		# only first agent says red or blue to indicate odd or even
		if(agent.size == n):
			print("Agent",agent.size,"announces:")
			number = countHats(agent,agents) # decide if the amount of red hats in front is even or odd
			print('"',number,'"')
			commonKnowledge.append(number) # the number of red hats is added as common knowledge
			updateKripke(model,agent,commonKnowledge,counter)
		else:
			color=deduceHatColour(agent,model,counter)
			print("Agent",agent.size,"announces:")
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
			printGraph(model,hats,counter)
	return commonKnowledge

def printGraph(m,h,counter):
	g = nx.MultiDiGraph() # create a multiGraph object
	realWorld=h.copy()
	realWorld.reverse()
	g.add_node(tuple(realWorld),style='filled',fillcolor='green')	# add the current world, in green
	for key,value in m.items():
		for w in range(0,len(value)):
			g.add_edge(tuple(realWorld),value[w],label=key,dir='both') # add an edge for each accessibility relations, nodes are created automatically. Each edge is labelled with the agent number	
	A = to_agraph(g)
	A.draw("kripkeModel"+str(counter)+".png", prog='dot') # print it to file
				
# update the model for each agent afer the announcements			
def updateKripke(m,a,commonKnowledge, counter):
	for agent,worlds in m.items(): 
		if(agent<a.size): #only update the knowledge of the agents in front of the agent that just spoke	
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
	worlds=m[a.size] # copy the worlds of a given agent
	knowsHat=0
	for w in range(0,len(worlds)):
		for nextWorld in range(1,len(worlds)):
			if(worlds[w][counter]==worlds[nextWorld][counter]): # compare if the element in the position of the agent is the same for all worlds
				color=worlds[w][counter]
				knowsHat=1
	if(knowsHat == 1):
		return color

# check if at most one mistake has been commited
def checkRiddle(c,h):
	h.reverse()
	numberOfMistakes=np.sum(c != h) # count number of dissimilar item
	if(numberOfMistakes == 0):
		print("Wow you are a highly intelligence specie, you will not be eaten!")
	elif(numberOfMistakes == 1):
		print("You are lucky, you made only one mistake so you will not be eaten!")
	else:
		print("Gnam gnam you all will be our dinner!!")


# runs Riddle 1		
def runRiddle1(a,number_prisoners,h):
	m=createAgentKnowledge(a,number_prisoners,h) # creates the initial kripke model
	c=announcementLoop(a,m,number_prisoners,h) # go in the announcement loop 
	checkRiddle(c,h)
	