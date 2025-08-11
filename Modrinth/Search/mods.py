import requests

import Modrinth.Convert.mods
from Modrinth.constants import *


def do(arguments):
    params = {"limit" : "100"}
    facets = '[["project_type:mod"]]'
    if "name" in arguments:
        params["query"] = arguments["name"]
    if "version" in arguments:
        facets = facets[:-1] + f",[\"versions={arguments["version"]}\"]]"
    if "mod_loader" in arguments:
        facets = facets[:-1] + f",[\"[categories:{arguments["mod_loader"]}]\"]]"
    if "offset" in arguments:
        params["offset"] = arguments["offset"]
    params["facets"] = facets
    print(facets)
    response = requests.get(f"{MODRINTH_API_URL}/search", params=params)
    if response.status_code == 404:
        return {}
    response = response.json()
    return Modrinth.Convert.mods.mods(response)