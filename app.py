from flask import Flask, send_from_directory, render_template, Response
import os

app = Flask(__name__)

# Map routes without .html
pages = ["", "about", "programmes", "team", "gallery", "partnerships", "contact", "citizens not spectators", "democracy in sa", "national-holidays", "national-symbols"]

@app.route("/")
@app.route("/<page>")
def serve_page(page="index"):
    try:
        return render_template(f"{page}.html")
    except Exception as e:
        # Show the exact error for debugging
        return f"Error rendering {page}.html: {e}", 500

# Serve robots.txt
@app.route("/robots.txt")
def robots_txt():
    content = """User-agent: *
Allow: /

Sitemap: https://ccd-za.onrender.com/sitemap.xml
"""
    return Response(content, mimetype="text/plain")

# Serve sitemap.xml
@app.route("/sitemap.xml")
def sitemap_xml():
    urls = [
        "https://ccd-za.onrender.com/",
        "https://ccd-za.onrender.com/about",
        "https://ccd-za.onrender.com/programmes",
        "https://ccd-za.onrender.com/team",
        "https://ccd-za.onrender.com/gallery",
        "https://ccd-za.onrender.com/partnerships",
        "https://ccd-za.onrender.com/contact"
    ]
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        sitemap_content += f"  <url>\n    <loc>{url}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
    sitemap_content += '</urlset>'
    return Response(sitemap_content, mimetype="application/xml")
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)




