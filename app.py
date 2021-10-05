from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/webapp")
def webapp():
    return jsonify(message='I am a webapp in Openshift.')

@app.route("/")
def main():
    return jsonify(message='Welcome to webapp from OpenShift. Trigger webhook!')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
