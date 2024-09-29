# Chess Move Visualizer

This is a Chess Move Visualizer web application that integrates Stockfish, an open-source chess engine, to suggest the best move based on the current position. The app allows users to drag and drop pieces on a chessboard, fetch the best move from Stockfish, and visualize the position updates in real time.

## Features

- Fully interactive chessboard with drag-and-drop functionality.
- Integration with Stockfish to calculate the best move.
- Flask-based backend that handles communication with Stockfish.
- FEN string generation to reflect the current state of the board.
- Displays the best move on the web page.

## Requirements

- Python 3.x
- Flask
- Stockfish chess engine
- chessboard.js for frontend visualization
