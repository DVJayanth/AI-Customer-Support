from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to AI-Powered Customer Support Backend!"})

if __name__ == "__main__":
    app.run(debug=True)

