from flask import Flask, jsonify, render_template
import chess
import chess.engine

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/best-move', methods=['GET'])
def get_best_move():
    # Set up the Stockfish engine
    with chess.engine.SimpleEngine.popen_uci('/usr/local/bin/stockfish') as engine:
        board = chess.Board()  # You can replace this with the current board state if needed
        result = engine.play(board, chess.engine.Limit(time=2.0))
        best_move = result.move

    # Return the best move in FEN format
    return jsonify({'fen': board.fen(), 'best_move': str(best_move)})

if __name__ == '__main__':
    app.run(port=3000)
