import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    message = os.environ.get("MESSAGE", "Bienvenue sur mon application Cloud !")
    return f"<h1>{message}</h1><p>Application Flask déployée sur Render.</p><p>Version 1</p>"

@app.route("/api/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)