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
    
# POST endpoint that accepts a JSON object representing a Tic-Tac-Toe board
@app.route('/api/board', methods=['POST'])
def handle_tic_tac_toe_board():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()

    # Validate that the input has exactly 9 keys (0 to 8) with valid values (either 'X', 'O', or '0')
    valid_keys = [str(i) for i in range(9)]
    valid_values = ['X', 'O', '0']

    # Check if all required keys are present and have valid values
    if sorted(data.keys()) != valid_keys or not all(item in valid_values for item in data.values()):
        return jsonify({"error": "Invalid board. Expecting 9 positions (0-8) with values 'X', 'O', or '0'."}), 400

    # Example logic: return the received board and a message
    return jsonify({"board": data, "message": "Board received successfully"}), 200)