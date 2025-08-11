def mods(initial):
    mods = initial["hits"]
    result = []
    for mod in mods:
        resulting_mod = {}
        try:
            resulting_mod["downloads"] = mod["downloads"]
            resulting_mod["slug"] = mod["slug"]
            resulting_mod["name"] = mod["title"]
            resulting_mod["logo"] = mod["icon_url"]
            resulting_mod["id"] = mod["project_id"]
        except KeyError:
            print(mod)
            resulting_mod["downloads"] = "-1"
            resulting_mod["slug"] = "undefined"
            resulting_mod["name"] = "undefined"
            resulting_mod["logo"] = "undefined"
            resulting_mod["id"] = "balls"
        resulting_mod["source"] = "modrinth"
        result.append(resulting_mod)
    return result