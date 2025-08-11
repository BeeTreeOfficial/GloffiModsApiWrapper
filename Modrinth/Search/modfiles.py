import requests

def do(arguments, id):
    params = {}
    if "version" in arguments:
        params["gameVersion"] = arguments["version"]
    if "mod_loader" in arguments:
        params["modLoaderType"] = arguments["mod_loader"]
    print(params)
    response = requests.get(f"{CURSEFORGE_API_URL}/mods/" + id + "/files", params=params, headers={"x-api-key": CURSEFORGE_API_KEY})
    responseJson = CurseForge.Convert.files.Do(response.json()) 
    return responseJson
