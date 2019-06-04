# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:26:47 2019

@author: danie and lucia
"""
import numpy as np 
import Agent
import Kripke
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
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
		
		
def createAgentKnowledge(agents,n):
	df = pd.DataFrame(columns=['Agent','hatColour','numberOfRedHats','numberOfBlueHats','K_agent(hatColour)'])
	for agent in reversed(agents):
		blueCount,redCount=countHats(agent,agents)
		df = df.append({'Agent': agent.size,'hatColour':agent.colourHat,'numberOfRedHats':redCount,'numberOfBlueHats':blueCount,'K_agent(hatColour)':'no'}, ignore_index=True)
	print(df)
	allWorlds=list(product(['blue','red'],repeat = n))
	print(allWorlds)

# creates the knowledge of each agent at the beginning of the riddle (before any announcements)		
def createAgentKnowledge(agents,n,hats):
	allWorlds=list(product(['blue','red'],repeat = n)) # creates all possible worlds
	kripke = Kripke.Kripke(agents,allWorlds,hats) # define a new Kripke model
	model=kripke.createKripkeModel()
	return model

def announcementLoop(agents,model,n):
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
			print(dict(m))
	return commonKnowledge

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
	
# contains the dialogue with the user	   
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
	else:
		print("Please input either yes or no")   
	m=createAgentKnowledge(a,number_prisoners,h)
	while True:
		kripkeChoice= str(input("Would you like to inspect the initial Kripke model? [yes/no] \n"))
		if (kripkeChoice != "yes" and kripkeChoice != "no"):
			print("Please enter either yes or no.")
			continue
		else:
			break
	if(kripkeChoice=="yes"):
		print("The Kripke model before any announcement is made is:")
		print(dict(m))
	c=announcementLoop(a,m,number_prisoners)
	checkRiddle(c,h)
    
    
        
  
        
        
        
        
        
        
        
        
        
        
        
        
