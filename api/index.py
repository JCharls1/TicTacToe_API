from flask import Flask, jsonify, request  # Added 'request'
import math

app = Flask(__name__)


# Function to check if there are any moves left on the board
def is_moves_left(board):
    return any(s == ' ' for s in board)

# Function to evaluate the board for a winner
def evaluate(board):
    # Winning combinations (row, column, and diagonal)
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    # Check for a winner
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            if board[combo[0]] == 'X':
                return 10  # AI wins
            elif board[combo[0]] == 'O':
                return -10  # Player wins

    return 0  # No winner

# Minimax function
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If AI wins
    if score == 10:
        return score - depth  # Subtract depth to choose quicker win

    # If Player wins
    if score == -10:
        return score + depth  # Add depth to delay loss

    # If no moves left, it's a draw
    if not is_moves_left(board):
        return 0

    # If it's the AI's turn (maximizing player)
    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, depth + 1, False))
                board[i] = ' '
        return best

    # If it's the player's turn (minimizing player)
    else:
        best = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, depth + 1, True))
                board[i] = ' '
        return best

# Function to find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 0, False)
            board[i] = ' '

            if move_val > best_val:
                best_val = move_val
                best_move = i

    return best_move

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
# @app.route('/api/board', methods=['POST'])
# def echo():
#     if request.is_json:
#         data = request.get_json()
#         return jsonify({"you_sent": data}), 200
#     else:
#         return jsonify({"error": "Request must be JSON"}), 400

@app.route('/api/board', methods=['POST'])
def echo():
    if request.is_json:
        data = request.get_json()

        # Convert the incoming data into a board list
        board = [' ']*9  # Initialize empty board
        for i in range(9):
            if str(i) in data:
                board[i] = data[str(i)]

        # Find the best move using Minimax
        best_move = find_best_move(board)

        return jsonify({"best_move": best_move}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

