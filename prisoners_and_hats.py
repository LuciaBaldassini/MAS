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

def assignRandomHat(n):
	agents = []  
    # obtain and store the colours of the hats
	#print("\nPlease type the colours of the hats of the prisoners from the smallest prisoner to the largest. \nPlease choose only \"red\" or \"blue\"")
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


def countHats(agent,agents):
	#numberBlueHats=0
	numberRedHats=0
	for a in agents[:agent.size-1]:
		#if(a.colourHat=='blue'):
			#numberBlueHats += 1
		if(a.colourHat=='red'):
			numberRedHats += 1
	if numberRedHats % 2 == 0:
		return 'red'
	else:
		return 'blue'
		
	
		
def createAgentKnowledge(agents,n,hats):
	#df = pd.DataFrame(columns=['Agent','hatColour','numberOfRedHats','numberOfBlueHats','K_agent(hatColour)'])
	#for agent in reversed(agents):
	#	blueCount,redCount=countHats(agent,agents)
	#	df = df.append({'Agent': agent.size,'hatColour':agent.colourHat,'numberOfRedHats':redCount,'numberOfBlueHats':blueCount,'K_agent(hatColour)':'no'}, ignore_index=True)
	# creates all possible worlds
	allWorlds=list(product(['blue','red'],repeat = n))
	kripke = Kripke.Kripke(agents,allWorlds,hats)
	model=kripke.createKripkeModel()
	print("The Kripke model before any announcement is made is:")
	print(dict(model))
	return model

def announcementLoop(agents,model):
	for agent in reversed(agents):
		if(agent.size != 1):
			print("Agent",agent.size,"announces:")
			number = countHats(agent,agents)
			print('"',number,'"')
			#model.updateKripke()
	
	   
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
		a,h=assignRandomHat(number_prisoners)
	m=createAgentKnowledge(a,number_prisoners,h)
	announcementLoop(a,m)

    
    
        
  
        
        
        
        
        
        
        
        
        
        
        
        
