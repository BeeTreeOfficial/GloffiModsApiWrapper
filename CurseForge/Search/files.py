import requests
import CurseForge.Convert.files
from CurseForge.constants import *

def do(arguments, id):
    params = {}
    if "version" in arguments:
        print("Detected Version")
        params["gameVersion"] = arguments["version"]
    if "mod_loader" in arguments and arguments["mod_loader"] in platform:
        print("Detected Modloader")
        params["modLoaderType"] = platform[arguments["mod_loader"]]
    print(params, "Are the parameters")
    response = requests.get(f"{CURSEFORGE_API_URL}/mods/" + id + "/files", params=params, headers={"x-api-key": CURSEFORGE_API_KEY})
    if response.status_code == 404:
        print("404")
        return {}    
    responseJson = CurseForge.Convert.files.Do(response.json()) 
    responseJson = separate_version_and_loader(responseJson)
    return responseJson

## Короче мне впадлу Regex самому писать, сори, через гемини ебану. Но остальное я сам писал.
import re

def separate_version_and_loader(data):
    processed_data = []
    # Regex to identify version numbers like "1.16.5"
    version_pattern = re.compile(r'^\d+\.\d+(\.\d+)?$')
    known_loaders = {"Forge", "NeoForge", "Quilt", "Fabric", "LiteLoader", "Cauldron"}

    for item in data:
        new_item = item.copy()

        mc_version = None
        loaders = []

        # Extract version and loaders from the 'versions' list
        for version_info in new_item.get('versions', []):
            if version_pattern.match(version_info):
                mc_version = version_info
            elif version_info in known_loaders:
                loaders.append(str(version_info).lower())
        
        # Add the new fields and remove the old one
        new_item['version'] = mc_version
        new_item['loaders'] = sorted(list(set(loaders))) # Sort for consistent order
        del new_item['versions']
        
        processed_data.append(new_item)

    return processed_data
