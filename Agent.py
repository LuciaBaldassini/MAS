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
        
	def __repr__(self): # for printing purposes, will be more elaborate once we add the knowledge tree
		ret = ""
		ret += "Agent "
		ret += repr(self.size)
		ret += " sees the following hats, from tallest to shortest:"
		ret += "\n"
		for hat in self.hats_in_front:
			ret += repr(hat)
		return ret
