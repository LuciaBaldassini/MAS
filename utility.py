import Agent
import numpy as np

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
		while (colour not in colorPossibility):
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
