import random

from passlib.hash import sha512_crypt

from dbcon import DBConnect
from mailing import sendcode 
from user import User 
import sqlite3


class UserRepo:
    db_connect = None
    
    def __init__(self, db_connect):
    	self.db_connect = sqlite3.connect('securite.db')
    
    def add_user(self, nom: str, prenom: str, email: str, pwd: str):
    	if self.get_user_by_email(email=email) is None:
    		password = sha512_crypt.hash(pwd)
    		cur = self.db_connect.cursor()
    		print("Adding User!")
    		cur.execute("INSERT INTO User(Nom, Prenom, Email, Pwd) VALUES (:name, :surname, :email, :pass)", {"name": nom, "surname": prenom, "email": email, "pass": password})
    		self.db_connect.commit()
    		print("User Added")
    	else:
    		raise Exception("User already exists!")
    
    def get_user_by_email(self, email: str):
    	user_email = (email)
    	cur = self.db_connect.cursor()
    	cur.execute("SELECT * from User where email=:mail", {"mail": user_email})
    	return cur.fetchone()
    
    def login(self, email: str, pwd: str):
    	res = self.get_user_by_email(email=email)
    	random_num = random.randint(100000,999999)
    	if res is None:
    		return False
    	user= User(query=res)
    	pwd_verif = sha512_crypt.verify(pwd, user.pwd)
    	if pwd_verif is True:
    		content= f"Code: {random_num}"
    		sendcode(user.email, random_num)
    		verif_code = int(input("Enter verification code: "))
    		if verif_code==random_num:
    			return True
    	return False
    
    
    