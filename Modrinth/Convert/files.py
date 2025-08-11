import json

def do(modrinth_data):
    Result = []
    modTemplate = {
        "name" : "0",
        "downloads" : "0",
        "url" : "0",
        "versions" : "0",
        "dependencies" : "0",
        "loaders" : []
    }
    for mod in modrinth_data:
        converted_mod = {}
        if "name" in mod:
            converted_mod["name"] = mod["name"]
        if "downloads" in mod:
            converted_mod["downloads"] = mod["downloads"]
        if "loaders" in mod:
            converted_mod["loaders"] = mod["loaders"]
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
        
def filter_mods_by_loader(mods_data, modloader):
  filtered_mods = []
  for mod in mods_data:
    if modloader in mod.get("loaders", []):
      filtered_mods.append(mod)
  return filtered_mods

def filter_mods_by_version(mods_data, version: str):
  filtered_mods = []
  for mod in mods_data:
    if version in mod.get("versions", []):
       filtered_mods.append(mod)
  return filtered_mods