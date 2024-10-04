# /api/index.py

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask Vercel Example - Hello World", 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello, welcome to the Flask API!"})

@app.route('/api/echo', methods=['POST'])
def echo():
    if request.is_json:
        data = request.get_json()
        return jsonify({"you_sent": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400
    
# POST endpoint that accepts an array of characters
@app.route('/api/board', methods=['POST'])
def handle_characters():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()

    # Validate that the data is a list of single characters
    if not isinstance(data, list) or not all(isinstance(item, str) and len(item) == 1 for item in data):
        return jsonify({"error": "Invalid input. Expecting an array of single characters."}), 400

    # Example logic: return the received characters in reverse order
    reversed_data = data[::-1]

    return jsonify({"original": data, "reversed": reversed_data}), 200