# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:26:47 2019

@author: danie
"""

class Agent:
    def __init__(self, size):
        self.size = size
        self.hats_in_front = []
        
    def __repr__(self): # for printing purposes, will be more elaborate once we add the knowledge tree
        ret = ""
        ret += "Agent "
        ret += repr(self.size)
        ret += " sees the following hats, from shortest to longest agent:"
        ret += "\n"
        for hat in self.hats_in_front:
            ret += repr(hat)
        return ret
    
    
if __name__ == '__main__':
    number_prisoners = int(input("Welcome, how many prisoners would you like? \n"))
    print("You chose", number_prisoners, "prisoners")
    
    agents = []
    
    # obtain and store the colours of the hats
    print("\nPlease type the colours of the hats of the prisoners from the smallest prisoner to the largest. \nPlease choose only \"red\" or \"blue\"")
    hats = []
    i = 0
    while i < number_prisoners:
        print("Agent", i, "has the following colour hat:")
        colour = input("")
        while (colour != "red" and colour != "blue"):
            print("Please choose only \"red\" or \"blue\"")
            print("Agent", i, "has the following colour hat:")
            colour = input("")
        new_agent = Agent(i)
        new_agent.hats_in_front = hats.copy()
        hats.append(colour) # add after so agents own hat is not added to list
        agents.append(new_agent)
        i += 1
    
    print("\n")
    # what all agents see
    for agent in agents:
        print(agent)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        