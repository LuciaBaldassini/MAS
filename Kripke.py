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
			if(a.id==1):
					self.model[a.id]= self.worlds
			else:
				subArray=self.hats[:a.id-1]
				for w in self.worlds:
					worldSubset=w[-len(subArray):len(w)]
					if(np.array_equal(list(reversed(subArray)),worldSubset)):
						self.model[a.id].append(w)
		return self.model
		
		
	
		
				
		
