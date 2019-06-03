# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:26:47 2019

@author: danie and lucia
"""
import numpy as np 
import Agent
import Kripke
import pandas as pd
from itertools import product

# randomly assign a hat colour to each agent
def assignRandomHat(n):
	agents = []  
	hats = []
	i = 1
	while i < number_prisoners+1:
		new_agent = Agent.Agent(i,1)
		new_agent.hats_in_front = hats.copy()
		hats.append(new_agent.colourHat)
		agents.append(new_agent)
		i += 1
	print("The agents are distributed like this (from tallest to shortest):",list(reversed(hats)))
	return agents,hats

# let the user assign a hat colour for each agent		
def assignHatUser(n):
	agents = []
	print("\nType the colours of the hats of the prisoners. \nPlease choose only \"red\" or \"blue\"")
	hats = []
	i = 1
	while i < number_prisoners+1:
		print("Agent", i, "has the following colour hat:")
		colour = input("")
		while (colour != "red" and colour != "blue"):
			print("Please choose only \"red\" or \"blue\"")
			print("Agent", i, "has the following colour hat:")
			colour = input("")
		new_agent = Agent.Agent(i,colour)
		new_agent.hats_in_front = hats.copy()
		hats.append(new_agent.colourHat) # add after so agents own hat is not added to list
		agents.append(new_agent)
		i += 1
	print("The agents are distributed like this (from tallest to shortest):",list(reversed(hats)))
	return agents,hats

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
		
	
<<<<<<< HEAD
		
def createAgentKnowledge(agents,n):
	df = pd.DataFrame(columns=['Agent','hatColour','numberOfRedHats','numberOfBlueHats','K_agent(hatColour)'])
	for agent in reversed(agents):
		blueCount,redCount=countHats(agent,agents)
		df = df.append({'Agent': agent.size,'hatColour':agent.colourHat,'numberOfRedHats':redCount,'numberOfBlueHats':blueCount,'K_agent(hatColour)':'no'}, ignore_index=True)
	print(df)
	allWorlds=list(product(['blue','red'],repeat = n))
	print(allWorlds)

=======
# creates the knowledge of each agent at the beginning of the riddle (before any announcements)		
def createAgentKnowledge(agents,n,hats):
	allWorlds=list(product(['blue','red'],repeat = n)) # creates all possible worlds
	kripke = Kripke.Kripke(agents,allWorlds,hats) # define a new Kripke model
	model=kripke.createKripkeModel()
	print("The Kripke model before any announcement is made is:")
	print(dict(model))
	return model

def announcementLoop(agents,model,n):
	for agent in reversed(agents):
		if(agent.size == n):
			print("Agent",agent.size,"announces:")
			number = countHats(agent,agents) # decide if the amount of red hats in front is even or odd
			print('"',number,'"')
		updateKripke(model,agent,number)
		print(dict(m))
		print('new loop')

# update the model for each agent afer the announcements			
def updateKripke(m,a,number):
	for agent,worlds in m.items(): 
		if(agent<a.size): #only update the knowledge of the agents in front of a given agent
			toRemove=[]
			for w in worlds:
				worldSubset=w[-(a.size-1):len(w)] # look in the subset world from the agent that just spoke till the end
				if(number=='red'):
					if(worldSubset.count('red') %2 != 0):
						toRemove.append(w) # append the world to be removed to a list
				else:
					if(w.worldSubset('red') %2 == 0):
						m[agent].remove(w)
			for i in toRemove: # remove the list of worlds from the dictionary
				m[agent].remove(i)
>>>>>>> lucia
	   
if __name__ == '__main__':
	while True:
		descriptionChoice= str(input("Welcome, would you like to read the description of this riddle? [yes/no] \n"))
		if (descriptionChoice != "yes" and descriptionChoice != "no"):
			print("Please enter either yes or no.")
			continue
		else:
			break
	if(descriptionChoice=="yes"):
		with open('description.txt', 'r') as d:
			print(d.read())
	while True:
		number_prisoners = int(input("How many prisoners would you like? \n"))
		if (number_prisoners<2):
			print("Please input at least 2 agents")
			continue
		else:
			break
	print("You chose", number_prisoners, "prisoners")
	while True:
		hatChoice=str(input("Do you want to choose a hat colour yourself for each agent (if not, this will be done automatically)[yes/no]?"))   
		if (hatChoice != "yes" and hatChoice != "no"):
			print("Please enter either yes or no.")
			continue
		else:
			break
	if(hatChoice=='yes'):
		a,h=assignHatUser(number_prisoners)
	elif(hatChoice=='no'):
<<<<<<< HEAD
		a=assignRandomHat(number_prisoners)
		print("This is the knowledge of the agents before any assignment:\n")
		createAgentKnowledge(a,number_prisoners)
	else:
		print("Please input either yes or no")   
=======
		a,h=assignRandomHat(number_prisoners)
	m=createAgentKnowledge(a,number_prisoners,h)
	#announcementLoop(a,m,number_prisoners)
>>>>>>> lucia

    
    
        
  
        
        
        
        
        
        
        
        
        
        
        
        
