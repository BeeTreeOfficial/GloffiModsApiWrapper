import requests
import CurseForge.Convert.files
from CurseForge.constants import *

def do(arguments, id):
    params = {}
    if "version" in arguments:
        params["gameVersion"] = arguments["version"]
    if "mod_loader" in arguments and arguments["mod_loader"] in platform:
        params["modLoaderType"] = platform[arguments["mod_loader"]]
    print(params)
    response = requests.get(f"{CURSEFORGE_API_URL}/mods/" + id + "/files", params=params, headers={"x-api-key": CURSEFORGE_API_KEY})
<<<<<<< Updated upstream
    responseJson = CurseForge.Convert.files.Do(response.json()) 
=======
    if response.status_code == 404:
        return {}
    responseJson = CurseForge.Convert.files.convert_mods(response.json()) 
>>>>>>> Stashed changes
    return responseJson


