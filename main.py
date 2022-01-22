import os
import subprocess
import threading
import auth
from dbcon import DBConnect
from phase3.menu import phase3Menu
from repo import UserRepo
from phase3.chat.chat import PeerToPeer

if __name__ == "__main__":
    user_choice = None
    
    def start_server():
        subprocess.call('python phase3/chat/server.py 9999', shell=True)

    def start_client():
        subprocess.call('python phase3/chat/client.py 9999', shell=True)
        
    conn = DBConnect()
    user_repo = UserRepo(db_connect=conn)
    while user_choice != 4:
        user_choice = int(
            input(
                "Enter your choice: \n"
                "1. To register a new user.\n"
                "2. To login a user.\n"
                "3. To Go to phase3.\n"
                "4. Chat\n"
            )
        )
        if user_choice == 1:
            auth.signup(user_repo=user_repo)
            print()
            print()
        elif user_choice == 2:
            auth.login(user_repo=user_repo)
            print()
            print()
        elif user_choice == 3:
            phase3Menu()
        elif user_choice == 4:
            client = PeerToPeer()
            client.menu()