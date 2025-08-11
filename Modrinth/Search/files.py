import requests

import Modrinth.Convert.files
from Modrinth.constants import *

def do(arguments, id):
    params = {}
    print(params)
    response = requests.get(f"{MODRINTH_API_URL}/project/{id}/version", params=params)
    print(response.url)
    if response.status_code == 404:
        print("404")
        return {}
    response = response.json()
    responseJson = Modrinth.Convert.files.do(response)
    if "version" in arguments:
        print(f"Version filtering by {arguments["version"]}")
        responseJson = Modrinth.Convert.files.filter_mods_by_version(responseJson, arguments["version"]) 
    if "mod_loader" in arguments:
        print(f"Mod loader filtering by {arguments["mod_loader"]}")
        responseJson = Modrinth.Convert.files.filter_mods_by_loader(responseJson, arguments["mod_loader"]) 
    return responseJson
