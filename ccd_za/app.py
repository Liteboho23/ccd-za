from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="frontend", static_url_path="")

# Map routes without .html
pages = ["", "about", "programmes", "team", "gallery", "partnerships", "contact"]

@app.route("/")
@app.route("/<path:path>")
def serve_page(path=None):
    if path is None or path == "":
        return send_from_directory(app.static_folder, "index.html")
    elif path.endswith("/"):
        return send_from_directory(app.static_folder, path + "index.html")
    else:
        return send_from_directory(app.static_folder, path)
# Serve other files like images, CSS, JS
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





