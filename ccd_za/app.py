from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../frontend")

# Serve static files (frontend pages)
@app.route('/')
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

# Example API endpoint (for contact form, newsletter, etc.)
@app.route('/api/test')
def api_test():
    return {"message": "Backend is working!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)