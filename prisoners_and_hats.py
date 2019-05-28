# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:26:47 2019

@author: danie and lucia
"""
import numpy as np 
import Agent
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
	#showHatDistribution(agents)
	return agents
		
# this function might not be necessary    
def showHatDistribution(agents):
	for agent in reversed(agents):
		print(agent)
		
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
	showHatDistribution(agents)
	return agents

def countHats(agent,agents):
	numberBlueHats=0
	numberRedHats=0
	for a in agents[:agent.size-1]:
		if(a.colourHat=='blue'):
			numberBlueHats += 1
		elif(a.colourHat=='red'):
			numberRedHats += 1
	return numberBlueHats,numberRedHats
		
	
		
def createAgentKnowledge(agents,n):
	df = pd.DataFrame(columns=['Agent','hatColour','numberOfRedHats','numberOfBlueHats','K_agent(hatColour)'])
	for agent in reversed(agents):
		blueCount,redCount=countHats(agent,agents)
		df = df.append({'Agent': agent.size,'hatColour':agent.colourHat,'numberOfRedHats':redCount,'numberOfBlueHats':blueCount,'K_agent(hatColour)':'no'}, ignore_index=True)
	allWorlds=list(product(['blue','red'],repeat = n))
	print(allWorlds)
	print(df)
	   
if __name__ == '__main__':
	descriptionChoice= str(input("Welcome, would you like to read the description of this riddle? [yes/no] \n"))
	if(descriptionChoice=="yes"):
		with open('description.txt', 'r') as d:
			print(d.read())
	number_prisoners = int(input("How many prisoners would you like? \n"))
	print("You chose", number_prisoners, "prisoners")
	hatChoice=str(input("Do you want to choose a hat colour yourself for each agent (if not, this will be done automatically)[yes/no]?"))   
	if(hatChoice=='yes'):
		a=assignHatUser(number_prisoners)
		print("This is the knowledge of the agents before any assignment:\n")
		createAgentKnowledge(a)
	elif(hatChoice=='no'):
		a=assignRandomHat(number_prisoners)
		print("This is the knowledge of the agents before any assignment:\n")
		createAgentKnowledge(a,number_prisoners)
	else:
		print("Please input either yes or no")   

    
    
        
  
        
        
        
        
        
        
        
        
        
        
        
        
