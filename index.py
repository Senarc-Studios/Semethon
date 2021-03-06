import subprocess
import sys
import cool_utils
import asyncio
import subprocess
import threading
import requests
from subprocess import PIPE, STDOUT
from requests import status_codes
from cool_utils import get_data
from local_cubacrypt import cypher as encrypt

cool_utils.JSON.open("config")
API = get_data("server")

def send_message(token, username, content):
	encrypted_string = encrypt(content)
	payload = {
		"token": token,
		"username": username,
		"esm": encrypted_string
	}
	requests.post(API + "send-message", json=payload)

def scan_for_content():
	subprocess.run(cool_utils.get_command("python") + " receiver.py", stdout=PIPE, stderr=STDOUT, shell=True, text=True)
	while True:
		if cool_utils.Cache.size() == 2:
			return
		else:
			message = cool_utils.Cache.load("message")
			content = message["message"]
			author = message["author"]
			print(f"<{author}> {message}")

def loop_input(token, username):
	while True:
		message = input(f"<{username}> ")
		send_message(token, username, message)

def create_session(username):
	payload = {
		"username": username
	}
	response = requests.post(API + "create-session", json=payload)
	if response.status_code == 200:
		print(f"Your Session has been created, here is your token.\n\nTOKEN: {response.json()['token']}.")

	payload = {
		"token": response.json()['token'],
		"username": username
	}

	utils.Cache.store("token", response.json()['token'])
	utils.Cache.store("username", username)

	thread = threading.Thread(target=scan_for_content, name="Message Scanner")
	thread.start()
	loop_input(payload["token"], username)

def join_session(token, username):
	payload = {
		"token": token,
		"username": username
	}
	response = requests.post(API + "join-session", json=payload)
	if response == 200:
		print(f"You have joined {response.json['host']}'s session.")

	else:
		print("Session token invalid.")

	utils.Cache.store("token", token)
	utils.Cache.store("username", username)

	thread = threading.Thread(target=scan_for_content, name="Message Scanner")
	thread.start()
	loop_input(token, username)

def validate_session(token):
	payload = {
		"token": token
	}
	response = requests.post(API + "validate-session", json=payload)
	if response.status_code == 200:
		return True
	else:
		return False

def execute_option(type):
	if type == "join":
		token = input("Enter session token: ")
		is_valid = validate_session(token)
		if is_valid == False:
			print("Invalid Session Token.")
			return execute_option(type)
		username = input("Enter your username: ")
		if len(username) >= 3 and len(username) <= 20:
			return join_session(token, username)

	elif type == "create":
		username = input("Enter your username: ")
		if len(username) >= 3 and len(username) <= 20:
			return create_session(username)

def selector():
	option = input("Do you want to join or create a session [Join/create]? ")
	if option.lower() == "j" or option.lower() == "join" or option == "":
		return execute_option("join")

	elif option.lower() == "c" or option.lower() == "create":
		return execute_option("create")

	else:
		print("Abort.")
		return sys.exit()

selector()
