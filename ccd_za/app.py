from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="frontend", static_url_path="")

# Map routes without .html
pages = ["", "about", "programmes", "team", "gallery", "partnerships", "contact"]

for page in pages:
    route_path = f"/{page}" if page else "/"
    file_name = "index.html" if page == "" else f"{page}.html"

    @app.route(route_path)
    def serve_page(file_name=file_name):
        return send_from_directory(app.static_folder, file_name)

# Serve other files like images, CSS, JS
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




