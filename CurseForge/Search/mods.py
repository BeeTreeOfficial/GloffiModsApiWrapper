from ast import arg
from http.client import responses
import requests
import CurseForge.Convert.mods
from CurseForge.constants import *

def search_mods_curseforge(arguments):
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
        params["modLoaderType"] = platform[arguments["mod_loader"]]
    
    response = requests.get(f"{CURSEFORGE_API_URL}/mods/search", params=params, headers={"x-api-key": CURSEFORGE_API_KEY})
    print(params, "Are the params of the request")
    print("The url is " + response.url)
    if response.status_code == 404:
        print("404!!")
        return {}
    responseJson = response.json()
    return CurseForge.Convert.mods.Do(responseJson)