import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Application Cloud</title>
        <style>
            body {
                font-family: Arial, Helvetica, sans-serif;
                margin: 0;
                padding: 16px;
                color: #1f2d3d;
            }
            h1 {
                color: #174a7c;
                font-size: 2rem;
                margin-bottom: 24px;
            }
            p {
                font-size: 1.1rem;
                margin-bottom: 16px;
            }
            img {
                border-radius: 10px;
                max-width: 950px;
                width: 100%;
                height: auto;
            }
            .credit, .version {
                font-size: 0.9rem;
                color: #666;
            }
        </style>
    </head>
    <body>
        <h1>Bienvenue sur mon application Cloud !</h1>
        <p>Cette application Flask est développée avec GitHub Codespaces et déployée sur Render.</p>
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Datacenter.jpg"
             alt="Baies de serveurs dans un centre de données">
        <p class="credit">Image : Datacenter.jpg -
        <a href="https://commons.wikimedia.org/wiki/File:Datacenter.jpg">Wikimedia Commons</a>.</p>
        <p class="version"><strong>Version 2</strong></p>
    </body>
    </html>
    """

@app.route("/api/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)