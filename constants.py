import os, sys
from dotenv import load_dotenv
load_dotenv()

DOWNLOADS_TRESHOLD = os.getenv("DOWNLOADS_TRESHOLD")

if not DOWNLOADS_TRESHOLD:
    DOWNLOADS_TRESHOLD = 1000
