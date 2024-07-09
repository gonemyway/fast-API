from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask import request

app = Flask(__name__)

CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin(origin='*')
def home():
    return "This is home!"

@app.route('/submit', methods=['POST'])
@cross_origin(origin='*')
def submit():
    #{
#        "name": "Sách AI",
 #       "price": 100000,
  #      "ready": 0
   # }
    request_json = request.json
    name = request_json["name"]
    price = request_json["price"]
    ready = request_json["ready"]

    if (name is None):
        return "Thiếu name"
    if (price is None):
        return "Thiếu price"
    if (ready is None):
        return "Thiếu ready"


    return "This is submit!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6868')