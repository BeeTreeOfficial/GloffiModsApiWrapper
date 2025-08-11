from flask import request

import Modrinth.Search.mods
import CurseForge.Search.mods

def search_mods(args):
    arguments = args
    print(arguments)
    jsonResponce = {
        "data" : [],
        "length" : "0"
    }
    try:
        jsonResponce["data"].extend(CurseForge.Search.mods.do(arguments))
    except:
        pass
    try:
        jsonResponce["data"].extend(Modrinth.Search.mods.do(arguments))
    except:
        pass
    jsonResponce["data"].sort(key=lambda mod: mod["downloads"], reverse=True)
    try:
        jsonResponce["data"] = jsonResponce["data"][:int(arguments["limit"])]
    except:
        pass
    jsonResponce["length"] = len(jsonResponce["data"])
    return jsonResponce
    