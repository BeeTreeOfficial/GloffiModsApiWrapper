from flask import request

import Modrinth.Search.mods
import CurseForge.Search.mods

def search_mods(args):
    print(args)
    jsonResponce = {
        "data" : [],
        "length" : "0"
    }
    try:
        jsonResponce["data"].extend(CurseForge.Search.mods.search_mods_curseforge(args))
    except:
        print("Error while retrieving CurseForge mods")
    try:
        jsonResponce["data"].extend(Modrinth.Search.mods.search_mods_modrinth(args))
    except:
        print("Error while retrieving Modrinth mods")
    jsonResponce["data"].sort(key=lambda mod: mod["downloads"], reverse=True)
    jsonResponce["data"] = [mod for mod in jsonResponce["data"] if mod['downloads'] >= 1000]
    try:
        jsonResponce["data"] = jsonResponce["data"][:int(args["limit"])]
    except:
        pass
    jsonResponce["length"] = len(jsonResponce["data"])
    return jsonResponce
    