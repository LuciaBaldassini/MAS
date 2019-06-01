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
			print(a.size)
			if(a.size==1):
					self.model[a.size]= self.worlds
			else:
				print('subarray')
				subArray=self.hats[:a.size-1]
				print(list(reversed(subArray)))
				for w in self.worlds:
					print('world')
					print(w)				
					print('subworld')
					worldSubset=w[-len(subArray):len(w)]
					print(worldSubset)	
					if(np.array_equal(list(reversed(subArray)),worldSubset)):
						self.model[a.size].append(w)
		return self.model
		
	
		
				
		
