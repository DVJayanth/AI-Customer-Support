import os
import signal
import socket
from flask import Flask, request, jsonify
from flask_cors import CORS

# Function to check if port 5000 is in use and kill the process
def free_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex(("127.0.0.1", port)) == 0:  # Port is in use
            pid = os.popen(f"lsof -ti :{port}").read().strip()  # Get PID
            if pid:
                os.kill(int(pid), signal.SIGKILL)  # Kill the process
        sock.close()
    except Exception as e:
        print(f"Error checking/freeing port {port}: {e}")

free_port(5000)  # Free port before starting Flask

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow frontend access

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to AI-Powered Customer Support Backend!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip().lower()

    # Simple bot responses
    bot_response = "I'm still learning! Stay tuned."
    if "hello" in user_message:
        bot_response = "Hello! How can I assist you?"
    elif "help" in user_message:
        bot_response = "Sure! Please describe your issue."

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
