from flask import Flask, jsonify, request  # Added 'request'

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Vercel Example - Hello World", 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

# A simple GET endpoint
@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello, welcome to the Flask API!"})

# A POST endpoint that accepts JSON data
@app.route('/api/echo', methods=['POST'])
def echo():
    if request.is_json:
        data = request.get_json()
        return jsonify({"you_sent": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400