import json

def do(modrinth_data):
    Result = []
    modTemplate = {
        "name" : "0",
        "downloads" : "0",
        "url" : "0",
        "versions" : "0",
        "dependencies" : "0",
    }
    for mod in modrinth_data:
        print(mod["name"])
        converted_mod = {}
        if "name" in mod:
            converted_mod["name"] = mod["name"]
        if "downloads" in mod:
            converted_mod["downloads"] = mod["downloads"]
        try:
            converted_mod["url"] = mod["files"][0]["url"]
        except:
            pass
        if "game_versions" in mod:
            converted_mod["versions"] = mod["game_versions"]
        if "dependencies" in mod:
            converted_mod["dependencies"] = [mod["project_id"] for mod in mod["dependencies"]  if mod.get("dependency_type") == "required"]
        Result.append(converted_mod)
    return Result
        