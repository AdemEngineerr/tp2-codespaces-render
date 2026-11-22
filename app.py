import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    message = os.environ.get(
        "MESSAGE",
        "Bienvenue sur mon application Cloud !"
    )
    return """
    <h1>Bienvenue sur mon application Cloud !</h1>
    <p>Cette application Flask est développée avec GitHub Codespaces et déployée sur Render.</p>
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Datacenter.jpg"
         alt="Baies de serveurs dans un centre de données"
         width="500">
    <p>Image : Datacenter.jpg -
    <a href="https://commons.wikimedia.org/wiki/File:Datacenter.jpg">
    Wikimedia Commons</a>.</p>
    <p><strong>Version 2</strong></p>
    """

@app.route("/api/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)