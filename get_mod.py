import CurseForge.Search.files
import Modrinth.Search.files

def get_mod(args, id):
    Responce = {"data": [],
                "length" : "0"}
    arguments = args
    if str(id).isdigit():
        print("Searching in CurseForge")
        Responce["data"].extend(CurseForge.Search.files.do(arguments, id))
    else:
        print("Searching in Modrinth")
        Responce["data"].extend(Modrinth.Search.files.do(arguments, id))
        
    Responce["length"] = len(Responce["data"])
    return Responce
