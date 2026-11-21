import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    Bienvenue sur mon application Cloud !
Cette application Flask est développée avec GitHub Codespaces et déployée sur Render.

Baies de serveurs dans un centre de données
Image : Datacenter.jpg – Wikimedia Commons (source de l'image).

Version 1
@app.route("/api/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)