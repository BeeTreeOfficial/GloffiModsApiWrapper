import os, sys
from dotenv import load_dotenv
load_dotenv()

CURSEFORGE_API_KEY = os.getenv('CURSEFORGE_API_KEY')
CURSEFORGE_API_URL = os.getenv('CURSEFORGE_API_URL')

if CURSEFORGE_API_KEY == None and CURSEFORGE_API_URL == None:
    print("CF Settings are missing")
    sys.exit(-1)
   
platform = {
    "forge" :  1,
    "cauldron" : 2,
    "liteloader" : 3,
    "fabric" : 4,
    "quilt" : 5,
    "neoforge" : 6,
}