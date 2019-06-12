# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:26:47 2019

@author:lucia
"""
import utility
import riddle1
import riddle2

	
# contains the dialogue with the user	   
if __name__ == '__main__':
	print("Welcome, I am a highly intelligent riddle solver and today I am challenging you to solve one of these two riddles (or both). Do you dare? Read the two riddle belows:")
	with open('description.txt', 'r') as d:
			print(d.read())
	while True:
		riddleChoice = int(input("Which riddle do you want to analyse? [1 or 2]"))
		if riddleChoice != 1 and riddleChoice!= 2 :
			print("Please choose either 1 or 2")
			continue
		else:
			break
	print("You chose riddle", riddleChoice)
	while True:
		number_prisoners = int(input("How many prisoners would you like? \n"))
		if number_prisoners<3:
			print("Please input at least 3 agents")
			continue
		else:
			break
	print("You chose", number_prisoners, "prisoners")
	while True:
		hatChoice=str(input("Do you want to choose a hat colour yourself for each agent (if not, this will be done automatically)[yes/no]?"))   
		if hatChoice != "yes" and hatChoice != "no":
			print("Please enter either yes or no.")
			continue
		else:
			break
	if hatChoice=='yes' and riddleChoice == 1 :
		a,h=utility.assignHatUser(number_prisoners,['blue','red'])
	elif hatChoice=='yes' and riddleChoice == 2 :
		a,h=utility.assignHatUser(number_prisoners,['blue','red','yellow'])
	elif hatChoice=='no' and riddleChoice ==1 :
		a,h=utility.assignRandomHat(number_prisoners,['blue','red'])
	elif hatChoice=='no' and riddleChoice ==2 :
		a,h=utility.assignRandomHat(number_prisoners,['blue','red','yellow'])
	else:
		print("Please input either yes or no")
	
	if  riddleChoice==1 :
		riddle1.runRiddle1(a,number_prisoners,h)
	elif riddleChoice==2 :
		riddle2.runRiddle2(a,number_prisoners,h)
    
    
        
  
        
        
        
        
        
        
        
        
        
        
        
        
