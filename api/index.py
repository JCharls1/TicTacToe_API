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
    
# POST endpoint that accepts a JSON object with an array under the "board" key
@app.route('/api/board', methods=['POST'])
def handle_board():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()

    # Validate that the "board" key exists and is an array of single characters
    if 'board' not in data or not isinstance(data['board'], list):
        return jsonify({"error": 'Invalid input. Expecting a "board" key with an array of characters.'}), 400

    board = data['board']

    # Validate that each element in the board is a single character string
    if not all(isinstance(item, str) and len(item) == 1 for item in board):
        return jsonify({"error": "Each item in the board array must be a single character."}), 400

    # Example logic: reverse the board array
    reversed_board = board[::-1]

    return jsonify({"original": board, "reversed": reversed_board}), 200