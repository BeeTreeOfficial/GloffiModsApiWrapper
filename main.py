import time
from flask import Flask, request
from search_mods import search_mods
from get_mod import get_mod

app = Flask(__name__)

errorJson = {
        "data" : [],
        "length" : "0"
    }

@app.route('/mods/search', methods=['GET'])
def search_mods_responce():
    beginning = time.time()
    try:
        print(f"Getting mod with this id: {id}")
        print(f"Time passed was {(time.time() - beginning) * 1000}")
        print(f"Searching with mods with arguments: \n{request.args}")
        return search_mods(request.args)
    except:
        return errorJson

@app.route('/mods/<id>') 
def ModInfo(id):
    beginning = time.time()
    try:
        print(f"Getting mod with this id: {id}")
        print(f"Time passed was {(time.time() - beginning) * 1000}")
        return get_mod(request.args, id)
    except:
        return errorJson

if __name__ == '__main__':
    app.run(debug=True)