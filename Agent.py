
# class Agent stores the agent id, the color of his own hat and the hat colors of the agents in front of him
class Agent:
	
	def __init__(self, id, color):
		self.id = id
		self.colourHat= color
		self.hats_in_front = []
