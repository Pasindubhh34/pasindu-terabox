from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Terabox Downloader API!"})

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing URL"}), 400
    return jsonify({
        "status": "success",
        "download_link": f"https://terabox-downloader.com/fake/{url}"
    })

# Vercel requires this handler
def handler(event, context):
    return app(event, context)
