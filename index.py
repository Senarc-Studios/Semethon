import sys
import asyncio
import threading
import requests
from requests import status_codes
from .local_cubacrypt import cypher as encrypt

API = "https://api.senarc.org/semethon/"

def send_message(token, content):
	encrypted_string = encrypt(content)
	payload = {
		"token": token,
		"esm": encrypted_string
	}
	response = requests.post(API + "send-message", payload=payload)
	if response.status_code == 200:
		print(f"<{response.json['username']}> {content}\n")

def scan_for_content(payload):
	response = requests.post(API + "fetch-messages", payload)
	if response.status_code == 404:
		return None
	else:
		message = requests.post(API + "decrypt", response.json())
		print(f"<{response['username']}> {message.json()}")

def create_session(username):
	payload = {
		"username": username
	}
	response = requests.post(API + "session/create", payload=payload)
	if response.status_code == 200:
		print(f"Your Session has been created, here is your token.\n\nTOKEN: {response.json['token']}.")

async def keep_alive(token, username):
	payload = {
		"token": token,
		"username": username
	}
	thread = threading.Thread(target=scan_for_content, name="Message Scanner", args=payload)
	thread.start()
	await asyncio.sleep(1)

def join_session(token, username):
	payload = {
		"token": token,
		"username": username
	}
	response = requests.post(API + "session/join", payload=payload)
	if response == 200:
		print(f"You have joined {response.json['host']}'s session.")

	else:
		print("Session token invalid.")

def validate_session(token):
	payload = {
		"token": token
	}
	response = requests.post(API + "validate", payload=payload)
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
		if username != "" and len(username) <= 3:
			return { "token": token, "username": username }

	elif type == "create":
		username = input("Enter your username: ")
		if username != "" and len(username) <= 3:
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
