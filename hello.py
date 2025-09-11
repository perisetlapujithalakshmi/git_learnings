from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello World"})

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"message": "Running on /status"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
