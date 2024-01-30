# pylint: disable-all
import secrets
import json


config = json.load(open("config.json", "r+"))
if config.get("client_id"):
    client_id = config.get("client_id")
else:  
    client_id = secrets.token_urlsafe(256)
