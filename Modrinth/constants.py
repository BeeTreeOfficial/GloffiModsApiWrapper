import os, sys
from dotenv import load_dotenv
load_dotenv()

MODRINTH_API_URL = os.getenv("MODRINTH_API_URL")

if not MODRINTH_API_URL:
    print("Modrinth`s Settings are missing")
    sys.exit(-1)
