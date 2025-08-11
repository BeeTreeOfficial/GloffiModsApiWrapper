from ast import arg
import requests
import CurseForge.Convert.mods
from CurseForge.constants import *

def do(arguments):
    params = {}
    params["gameId"] = "432"
    params["pageSize"] = "50"
    params["classId"] = "6"
    params["sortField"] = "6"
    params["sortOrder"] = "desc"
    if "name" in arguments:
        params["searchFilter"] = arguments["name"]
    if "version" in arguments:
        params["gameVersion"] = arguments["version"]
    if "offset" in arguments:
        params["index"] = arguments["offset"]
    if "mod_loader" in arguments:
        params["modLoaderType"] = platform.get(arguments["mod_loader"])
    
    print(params)
    response = requests.get(f"{CURSEFORGE_API_URL}/mods/search", params=params, headers={"x-api-key": CURSEFORGE_API_KEY})
    responseJson = response.json()
    return CurseForge.Convert.mods.Do(responseJson)