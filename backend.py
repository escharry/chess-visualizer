from flask import Flask, jsonify, render_template, request
import chess
import chess.engine

app = Flask(__name__)

STOCKFISH_PATH = "/usr/local/bin/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/best-move', methods=['POST'])
def best_move():
    data = request.get_json()
    current_fen = data['fen']  # Get current FEN from the request

    # Set up the chess board with the current FEN
    board = chess.Board(current_fen)

    # Get Stockfish's best move
    result = engine.play(board, chess.engine.Limit(time=2.0))  # 2 seconds for analysis
    board.push(result.move)  # Make the best move

    # Return the updated board FEN after the best move
    return jsonify({'fen': board.fen(), 'best_move': str(result.move)})

if __name__ == '__main__':
    app.run(port=3000)
