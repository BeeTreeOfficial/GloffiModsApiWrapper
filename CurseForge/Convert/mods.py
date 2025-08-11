def Do(Initial):
    mods = Initial["data"]
    Result = []
    for mod in mods:
        ResultingMod = {
            "source" : "curseforge"
        }   
        ResultingMod["downloads"] =mod["downloadCount"]
        ResultingMod["slug"] = mod["slug"]
        ResultingMod["name"] = mod["name"]
        ResultingMod["id"] = mod["id"]
        ResultingMod["about"] = mod["summary"]
        try:
            ResultingMod["logo"] = mod["logo"]["thumbnailUrl"]
        except:
            ResultingMod["logo"] = "https://cdn-icons-png.flaticon.com/512/1178/1178479.png"
        Result.append(ResultingMod)
    
    return Result
