from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="frontend", static_url_path="")

# Serve HTML files
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_page(path):
    return send_from_directory(app.static_folder, path)

# Railway will set the PORT variable automatically
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


