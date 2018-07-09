from flask import Flask
from flask_restful import Api, request

app = Flask("api-ml")
api = Api(app)

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World"

@app.route("/file", methods=["POST"])
def file():
    if "file" in request.files:
        f = request.files['file']
        f.save(f.filename)
    else:
        return "Arquivo não encontrado"

    return f.filename

app.run(host = "0.0.0.0", port = 8080, debug = True)