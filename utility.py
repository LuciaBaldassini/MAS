import Agent
import numpy as np
from pygraphviz import *
import graphviz
from itertools import product
from collections import defaultdict


# randomly assign a hat colour to each agent
def assignRandomHat(n,colorPossibility):
	agents = []  
	hats = []
	i = 1
	while i < n+1:
		new_agent = Agent.Agent(i,np.random.choice(colorPossibility))
		new_agent.hats_in_front = hats.copy()
		hats.append(new_agent.colourHat)
		agents.append(new_agent)
		i += 1
	print("The agents are distributed like this (from tallest to shortest):",list(reversed(hats)))
	return agents,hats

# let the user assign a hat colour for each agent		
def assignHatUser(n,colorPossibility):
	agents = []
	print("\nType the colours of the hats of the prisoners. \nPlease choose only \"red\" or \"blue\"")
	hats = []
	i = 1
	while i < n+1:
		print("Agent", i, "has the following colour hat:")
		colour = input("")
		while colour not in colorPossibility:
			print("Please choose only", colorPossibility)
			print("Agent", i, "has the following colour hat:")
			colour = input("")
		new_agent = Agent.Agent(i,colour)
		new_agent.hats_in_front = hats.copy()
		hats.append(new_agent.colourHat) # add after so agents own hat is not added to list
		agents.append(new_agent)
		i += 1
	print("The agents are distributed like this (from tallest to shortest):",list(reversed(hats)))
	return agents,hats

# creates the knowledge of each agent at the beginning of the riddle (before any announcements) and optionally prints it
def createAgentKnowledge(agents,n,hats,colorChoices):
	model = defaultdict(list)
	allWorlds=list(product(colorChoices,repeat = n)) # creates all possible worlds by finding all possible combinations of red, blue (and yellow in the case of riddle 2)
	for a in agents:
		if (a.id == 1): # the shortest agent have access to all possible worlds
			model[a.id] = allWorlds
		else:
			subArray = hats[:a.id - 1] # the worlds accessible for the other agents are those containing the color hats of the agents they see and all possible combinations of colors for the agents behind them (because they cannot see them)
			for w in allWorlds:
				worldSubset = w[-len(subArray):len(w)]
				if (np.array_equal(list(reversed(subArray)), worldSubset)):
					model[a.id].append(w)
	while True:
		kripkeChoice= str(input("Would you like to inspect the initial Kripke model (a nice fancy graph will be saved in the same folder as this programme)? [yes/no] \n"))
		if kripkeChoice != "yes" and kripkeChoice != "no":
			print("Please enter either yes or no.")
			continue
		else:
			break
	if kripkeChoice=="yes":
		printGraph(model,hats,0,1)
	return model
	
def printGraph(m,h,counter,riddleNumber):
	#path = Path("KripkeModels") / ("Riddle" + str(riddleNumber))
	filename="model"+str(counter)+".png"
	#if not path.is_dir():
	#	path.mkdir(parents=True)
	g=AGraph(rankdir='LR',ratio='auto')
	realWorld=h.copy()
	realWorld.reverse()
	g.add_node(tuple(realWorld),style='filled',fillcolor='green')	# add the current world, in green
	for key,value in m.items():
		l = printEdgeLabel(m,key)
		for w in range(0,len(value)):
			g.add_edge(tuple(realWorld),value[w],label=l,dir='both') # add an edge for each accessibility relations, nodes are created automatically. Each edge is labelled with the agent number
	#os.chdir(str(path))
	g.draw(filename,prog='dot') # print it to file

def printEdgeLabel(m,k):
	label=[]
	for key in m.keys():
		if key<=k:
			label.append(key)
	return label