import CurseForge.Search.modfiles
import Modrinth.Search.modfiles

def get_mod(args, id):
    Responce = {"data": []}
    arguments = args
    if str(id).isdigit():
        Responce["data"].extend(CurseForge.Search.modfiles.do(arguments, id))
    else:
        Responce["data"].extend(Modrinth.Search.modfiles.do(arguments, id))
    Responce["length"] = len(Responce["data"])
    return Responce
