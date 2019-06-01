from itertools import product
import numpy as np
from collections import defaultdict

class Kripke:
	def __init__(self, agents,worlds,hats):
		self.worlds = worlds
		self.agents = agents
		self.hats = hats
		self.model= defaultdict(list) 
		
        
	def createKripkeModel(self):
		for a in self.agents:
			if(a.size==1):
					self.model[a.size]= self.worlds
			else:
				subArray=self.hats[:a.size-1]
				for w in self.worlds:
					worldSubset=w[-len(subArray):len(w)]	
					if(np.array_equal(subArray,worldSubset)):
						self.model[a.size].append(w)
		return self.model
		
