import requests

import Modrinth.Convert.mods
from Modrinth.constants import *


def search_mods_modrinth(arguments):
    params = {"limit" : "100"}
    facets = '[["project_type:mod"]]'
    if "name" in arguments:
        params["query"] = arguments["name"]
    if "version" in arguments:
        facets = facets[:-1] + f",[\"versions={arguments["version"]}\"]]"
    if "mod_loader" in arguments:
        facets = facets[:-1] + f", [\"categories:{arguments["mod_loader"]}\"]]"
    if "offset" in arguments:
        params["offset"] = arguments["offset"]
    params["facets"] = facets
    response = requests.get(f"{MODRINTH_API_URL}/search", params=params)
    print(params, "Are the params of the request")
    print("The url is " + response.url)
    if response.status_code == 404:
        print("404")
        return {}
    response = response.json()
    return Modrinth.Convert.mods.mods(response)