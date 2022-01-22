import sqlite3




class DBConnect(object):
	db_connect = None
	
	def __init__(self):
		self.db_connect = sqlite3.connect('securite.db')
		
	def __str__(self):
		return "DB Con object"