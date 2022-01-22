class User:
	id: int
	email: str
	nom: str
	prenom: str
	pwd: str
	
	def __init__(self, query):
		self.nom = query[0]
		self.prenom= query[1]
		self.email = query[2]
		self.pwd = query[3]