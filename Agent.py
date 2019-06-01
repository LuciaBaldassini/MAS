import numpy as np 
hatColour=['blue','red']

class Agent:
	
	def __init__(self, size,randomColour):
		self.size = size
		if(randomColour==1):
			self.colourHat= np.random.choice(hatColour)
		else:
			self.colourHat= randomColour
		self.hats_in_front = []
		
        
