import time
import utils
import requests

API = utils.get_data('config', 'server')

def scan():
	while True:
		payload = {
			"token": utils.Cache.load("token"),
			"username": utils.Cache.load("username")
		}
		response = requests.post(API + "fetch-messages", json=payload)
		if response.status_code == 404:
			return None
		else:
			message = requests.post(API + "decrypt", response.json())
			print(f"<{response.json()['author']}> {message.json()['message']}")

		time.sleep(1)

scan()