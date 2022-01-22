import getpass
import re

from repo import UserRepo

def check_constraints(email: str, pwd: str, pwd_confirm: str):
	verified = False
	mail_regex = r"\b[A-Za-z0-9]+\.[A-Za-z0-9]+@insat.ucar.tn\b"
	if (re.fullmatch(mail_regex, email) and pwd == pwd_confirm and len(pwd) > 6):
		verified = True
	return verified


def getname(email: str):
	prenom, nom = email.split("@")[0].split(".")
	return prenom, nom
	
def signup(user_repo: UserRepo):
	print("				SignUp				")
	verified = False
	email =None
	pwd = None
	while not verified:
		email = str(input("Enter your email: "))
		pwd = getpass.getpass("Enter your password: ")
		pwd_confirm = getpass.getpass("Enter your password confirmation: ")
		verified = check_constraints(email=email, pwd=pwd, pwd_confirm=pwd_confirm)
		prenom, nom = getname(email=email)
	try:
		user_repo.add_user(nom=nom, prenom=prenom, email=email, pwd=pwd)
	except:
		print("This user already exists please try another user!")
		signup(user_repo=user_repo)
        
def login(user_repo: UserRepo):
	print("					Login						")
	email = None
	pwd = None
	while email is None and pwd is None:
		email = str(input("Enter your email: "))
		pwd = getpass.getpass("Enter your password: ")
	login_result = user_repo.login(email=email, pwd=pwd)
	if login_result is True:
		print("Login Successful!")
	else:
		print("Please verify your email and password!")