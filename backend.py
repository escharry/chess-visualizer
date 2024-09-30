import threading
from flask import Flask, jsonify, render_template, request
import chess
import chess.engine

app = Flask(__name__)

STOCKFISH_PATH = "/usr/local/bin/stockfish"
engine_eval = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
engine_move = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

eval_lock = threading.Lock()
move_lock = threading.Lock()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/evaluation", methods=["POST"])
def evaluation():
    data = request.get_json()
    fen = data['fen']
    board = chess.Board(fen)

    with eval_lock:  # Lock only for the evaluation engine
        try:
            result = engine_eval.analyse(board, chess.engine.Limit(time=2.0))  # Analyze for 2 seconds
            eval_score = result['score'].relative.score(mate_score=10000)  # Get evaluation score
            return jsonify({"evaluation": eval_score})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route("/best-move", methods=["POST"])
def best_move():
    data = request.get_json()
    fen = data['fen']
    board = chess.Board(fen)

    with move_lock:  # Lock only for the best move engine
        try:
            result = engine_move.play(board, chess.engine.Limit(time=2.0))  # Analyze for 2 seconds
            best_move = result.move.uci()
            return jsonify({"best_move": best_move})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)
