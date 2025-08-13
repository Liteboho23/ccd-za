from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# Map routes without .html
pages = ["", "about", "programmes", "team", "gallery", "partnerships", "contact", "citizens not spectators", "democracy in sa", "national holidays", "national symbols"]

@app.route("/")
@app.route("/<page>")
def serve_page(page="index"):
    try:
        return render_template(f"{page}.html")
    except Exception as e:
        # Show the exact error for debugging
        return f"Error rendering {page}.html: {e}", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)

