import requests
import cool_utils
from typing import Union

cache = {}
cool_utils.JSON.open("config")

class HTTPClient:
    def __init__(self):
        self.username = None
        self.token = None
        self.BASE = cool_utils.JSON.get_data("server")

    @classmethod
    def create_request(
        self,
        type: str,
        route: str,
        payload: dict = None,
        args: dict = None
    ):
        if type == "GET":
            if route.startswith("/") == False:
                route = "/" + route

            arg = ""

            for key, value in args:
                if arg == "":
                    arg = arg + key + "=" + value
                else:
                    arg = arg + "&" + key + "=" + value
            
            response = requests.get(HTTPClient.BASE + route + "?" + arg, json=payload)
            
            return response

        elif type == "POST":
            if route.startswith("/") == False:
                route = "/" + route

            payload['username'] = self.username
            
            if self.token != None:
                payload['token'] = self.token

            response = requests.post(HTTPClient.BASE + route, json=payload)

            return response

        elif type == "DELETE":
            if route.startswith("/") == False:
                route = "/" + route

            payload['username'] = self.username
            
            if self.token != None:
                payload['token'] = self.token

            response = requests.delete(HTTPClient.BASE + route, json=payload)

            return response

    @classmethod
    def create_session(self, username):
        self.username = username
        token = HTTPClient.create_request("POST", "create-session").json()['token']
        self.token = token
        return token

    @staticmethod
    def delete_session():
        return HTTPClient.create_request("DELETE", "delete-session")