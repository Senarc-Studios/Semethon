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
	response = requests.post(API, payload=payload)
	if response.status_code == 200:
		print(f"<{response.json['username']}> {content}\n")

def scan_for_content(token, username):
	payload = {
		"token": token,
		"username": username
	}
	response = requests.post(API + "message-updates", payload)
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