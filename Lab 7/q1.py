
import copy

EMPTY = '.'
WHITE = 'W'
BLACK = 'B'

BOARD_SIZE = 8
MAX_DEPTH = 3

def init_board():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    for row in range(3):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = BLACK

    for row in range(5, 8):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = WHITE
    return board

def print_board(board):
    for i in range(BOARD_SIZE):
        print(' '.join(board[i]))
    print()

def is_valid(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def get_moves(board, player):
    directions = [(-1, -1), (-1, 1)] if player == WHITE else [(1, -1), (1, 1)]
    captures = []
    normal_moves = []

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] != player:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and board[nx][ny] == EMPTY:
                    normal_moves.append(((x, y), (nx, ny)))
                elif is_valid(nx, ny) and board[nx][ny] != player and board[nx][ny] != EMPTY:
                    cx, cy = x + 2*dx, y + 2*dy
                    if is_valid(cx, cy) and board[cx][cy] == EMPTY:
                        captures.append(((x, y), (cx, cy)))
    return captures if captures else normal_moves

def apply_move(board, move):
    start, end = move
    x1, y1 = start
    x2, y2 = end
    player = board[x1][y1]
    board[x1][y1] = EMPTY
    board[x2][y2] = player

    # Handle captures
    if abs(x2 - x1) == 2:
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        board[mx][my] = EMPTY
        return True  # Capture happened
    return False

def minimax(board, depth, maximizing, alpha, beta):
    player = BLACK if maximizing else WHITE
    moves = get_moves(board, player)

    if depth == 0 or not moves:
        return evaluate_board(board), None

    best_move = None

    if maximizing:
        max_eval = float('-inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            apply_move(new_board, move)
            eval_score, _ = minimax(new_board, depth - 1, False, alpha, beta)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            apply_move(new_board, move)
            eval_score, _ = minimax(new_board, depth - 1, True, alpha, beta)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

def evaluate_board(board):
    white = sum(row.count(WHITE) for row in board)
    black = sum(row.count(BLACK) for row in board)
    return black - white  # AI is BLACK

def check_winner(board):
    white_moves = get_moves(board, WHITE)
    black_moves = get_moves(board, BLACK)

    white_pieces = sum(row.count(WHITE) for row in board)
    black_pieces = sum(row.count(BLACK) for row in board)

    if white_pieces == 0 or not white_moves:
        return "AI Wins!"
    if black_pieces == 0 or not black_moves:
        return "Human Wins!"
    return None

def main():
    board = init_board()
    print("Welcome to Checkers! You are White (W). AI is Black (B).\n")
    print_board(board)

    while True:
        # Human Turn
        player_moves = get_moves(board, WHITE)
        if not player_moves:
            print("No valid moves for player. AI wins!")
            break

        print("Your Move Options:")
        for idx, move in enumerate(player_moves):
            print(f"{idx}: {move[0]} -> {move[1]}")
        try:
            move_index = int(input("Select your move: "))
            move = player_moves[move_index]
            is_capture = apply_move(board, move)
            print(f"Player moves: {move[0]} -> {move[1]}" + (" [Capture!!]" if is_capture else ""))
            print_board(board)
        except:
            print("Invalid input! Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print(winner)
            break

        # AI Turn
        _, best_move = minimax(board, MAX_DEPTH, True, float('-inf'), float('inf'))
        if not best_move:
            print("AI has no valid moves. You win!")
            break
        is_capture = apply_move(board, best_move)
        print(f"AI moves: {best_move[0]} -> {best_move[1]}" + (" [Capture!!]" if is_capture else ""))
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(winner)
            break

if __name__ == "__main__":
    main()
