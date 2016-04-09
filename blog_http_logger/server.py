from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
    for k,v in request.args.items():
        print(k,v)
    return 'response' # it has to return something


if __name__ == "__main__":
    app.run(debug=True)
