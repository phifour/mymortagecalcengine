from mortgage import *

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={"/loan/*": {"origins": "*"}})

@app.route("/loan/<f>/<n>/<r>")
def mortgage(f,n,r):
    return calc_mortgage(f,n,r)
