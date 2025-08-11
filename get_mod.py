import CurseForge.Search.files
import Modrinth.Search.files

def get_mod(args, id):
    Responce = {"data": []}
    arguments = args
    if str(id).isdigit():
        Responce["data"].extend(CurseForge.Search.files.search_files(arguments, id))
    else:
        print("IM WORKING")
        Responce["data"].extend(Modrinth.Search.files.do(arguments, id))
        
    Responce["length"] = len(Responce["data"])
    return Responce
