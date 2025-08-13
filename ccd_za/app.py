from flask import Flask, render_template, send_from_directory
import os

app = Flask(
    __name__,
    static_folder="../Frontend",  # Serve static files (images, CSS, JS)
    template_folder="../Frontend"  # Serve HTML files
)

# Serve main pages
@app.route("/")
def home():
    return send_from_directory(app.template_folder, "index.html")

@app.route("/<path:filename>")
def serve_page(filename):
    file_path = os.path.join(app.template_folder, filename)
    if os.path.exists(file_path):
        return send_from_directory(app.template_folder, filename)
    else:
        return "Page not found", 404

# Serve Images, CSS, JS from Frontend/
@app.route("/Images/<path:filename>")
def serve_images(filename):
    return send_from_directory(os.path.join(app.static_folder, "Images"), filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway sets PORT env var
    app.run(host="0.0.0.0", port=port)
