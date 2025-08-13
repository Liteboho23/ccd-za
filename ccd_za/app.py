from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# Map routes without .html
pages = ["", "about", "programmes", "team", "gallery", "partnerships", "contact"]

@app.route("/")
@app.route("/<page>")
def serve_page(page="index"):
    try:
        return render_template(f"{page}.html")
    except:
        return render_template("404.html"), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)