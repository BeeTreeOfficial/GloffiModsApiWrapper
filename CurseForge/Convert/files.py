def convert_mods(Input):
    Result = []
    modTemplate = {
        "name" : "0",
        "downloads" : "0",
        "url" : "0",
        "versions" : "0",
        "dependencies" : "0",
    }
    for mod in Input["data"]:
        converted_mod = modTemplate.copy()
        converted_mod["name"] = mod["displayName"]
        converted_mod["downloads"] = mod["downloadCount"]
        converted_mod["url"] = mod["downloadUrl"]
        converted_mod["versions"] = mod["gameVersions"]
        converted_mod["dependencies"] = mod["dependencies"]
        converted_mod["dependencies"] = remove_non_required_dependencies(converted_mod["dependencies"])
        Result.append(converted_mod)
    return Result

def remove_non_required_dependencies(ListOfDependencies):
    dependencies_amount = len(ListOfDependencies)
    cleared_dependencies = []
    if dependencies_amount <= 0:
        return cleared_dependencies
    
    for Index in range(dependencies_amount):
        dependency = ListOfDependencies[Index]
        if str(dependency["relationType"]) == "3":   
            cleared_dependencies.append(dependency["modId"])
    
    return cleared_dependencies