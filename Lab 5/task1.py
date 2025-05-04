import chess
import chess.engine
import heapq

# Material count evaluator (simplistic)
def evaluate_board(board):
    values = {
        chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
        chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0
    }
    score = 0
    for piece_type in values:
        score += len(board.pieces(piece_type, chess.WHITE)) * values[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * values[piece_type]
    return score

# Beam search for best move sequence
def beam_search_best_move(board, beam_width=3, depth_limit=3):
    # Each entry: (score, [move1, move2, ...], board_after_moves)
    beam = [ (evaluate_board(board), [], board.copy()) ]

    for depth in range(depth_limit):
        next_beam = []
        for score, move_sequence, b in beam:
            if b.is_game_over():
                continue
            for move in b.legal_moves:
                b_copy = b.copy()
                b_copy.push(move)
                new_score = evaluate_board(b_copy)
                heapq.heappush(next_beam, (-new_score, move_sequence + [move], b_copy))
        
        # Prune to keep top `beam_width` (convert back to positive score)
        beam = [(-score, seq, b) for score, seq, b in heapq.nsmallest(beam_width, next_beam)]

    best_score, best_moves, _ = max(beam, key=lambda x: x[0])
    return best_moves, best_score

# Example usage
board = chess.Board()  # Initial position
beam_width = 3
depth_limit = 2

best_moves, score = beam_search_best_move(board, beam_width, depth_limit)

print("Best Move Sequence:")
for move in best_moves:
    print(board.san(move))
    board.push(move)
print("Evaluation Score:", score)

