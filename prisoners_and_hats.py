# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:26:47 2019

@author: danie
"""
import numpy as np 
import Agent


def assignRandomHat(n):
	agents = []  
    # obtain and store the colours of the hats
	#print("\nPlease type the colours of the hats of the prisoners from the smallest prisoner to the largest. \nPlease choose only \"red\" or \"blue\"")
	hats = []
	i = 1
	while i < number_prisoners+1:
		new_agent = Agent.Agent(i)
		new_agent.hats_in_front = hats.copy()
		hats.append(new_agent.colourHat)
		agents.append(new_agent)
		#print("Agent", i, "has the following colour hat:")
		#colour = input("")
		#while (colour != "red" and colour != "blue"):
		#	print("Please choose only \"red\" or \"blue\"")
		#	print("Agent", i, "has the following colour hat:")
		#	colour = input("")
		#new_agent = Agent(i)
		#new_agent.hats_in_front = hats.copy()
		#hats.append(colour) # add after so agents own hat is not added to list
		#agents.append(new_agent)
		i += 1
	showHatDistribution(agents)
		
    
def showHatDistribution(agents):
	for agent in reversed(agents):
		print(agent)
	   
if __name__ == '__main__':
	descriptionChoice= str(input("Welcome, would you like to read the description of this riddle? [yes/no] \n"))
	if(descriptionChoice=="yes"):
		with open('description.txt', 'r') as d:
			print(d.read())
	number_prisoners = int(input("How many prisoners would you like? \n"))
	print("You chose", number_prisoners, "prisoners")   
	assignRandomHat(number_prisoners)
    

    
    
        
  
        
        
        
        
        
        
        
        
        
        
        
        
