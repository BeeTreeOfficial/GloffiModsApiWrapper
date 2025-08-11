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
    return search_mods(request.args)

@app.route('/mods/<id>') 
def ModInfo(id):
    return get_mod(request.args, id)

if __name__ == '__main__':
    app.run(debug=True)