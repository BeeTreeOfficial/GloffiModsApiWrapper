import requests

import Modrinth.Convert.files
from Modrinth.constants import *

def do(arguments, id):
    params = {}
    if "version" in arguments:
        params["gameVersion"] = f"[\"{arguments["version"]}\"]"
    if "mod_loader" in arguments:
        params["loaders"] = "[\"" + arguments["mod_loader"] + "\"]"
    print(params)
    response = requests.get(f"{MODRINTH_API_URL}/project/{id}/version")
    response = response.json()
    responseJson = Modrinth.Convert.files.do(response) 
    return responseJson
