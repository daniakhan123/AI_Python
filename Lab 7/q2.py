def alphabeta(cards, left, right, is_max_turn, alpha, beta):
    if left > right:
        return 0, []

    if is_max_turn:
        max_eval = float('-inf')
        best_move = None
        # Max picks left
        val1, seq1 = alphabeta(cards, left + 1, right, False, alpha, beta)
        val1 += cards[left]
        if val1 > max_eval:
            max_eval = val1
            best_move = ['L'] + seq1

        alpha = max(alpha, max_eval)
        if beta <= alpha:
            return max_eval, best_move

        # Max picks right
        val2, seq2 = alphabeta(cards, left, right - 1, False, alpha, beta)
        val2 += cards[right]
        if val2 > max_eval:
            max_eval = val2
            best_move = ['R'] + seq2

        return max_eval, best_move
    else:
        # Min picks greedily: pick smaller of the two ends
        if cards[left] <= cards[right]:
            return alphabeta(cards, left + 1, right, True, alpha, beta)
        else:
            return alphabeta(cards, left, right - 1, True, alpha, beta)


def play_game(cards):
    max_score = 0
    min_score = 0
    left = 0
    right = len(cards) - 1
    turn = 'Max'

    print(f"Initial Cards: {cards}")

    while left <= right:
        if turn == 'Max':
            _, move_sequence = alphabeta(cards, left, right, True, float('-inf'), float('inf'))
            move = move_sequence[0] if move_sequence else 'L'
            if move == 'L':
                chosen = cards[left]
                left += 1
            else:
                chosen = cards[right]
                right -= 1
            max_score += chosen
            print(f"Max picks {chosen}, Remaining Cards: {cards[left:right+1]}")
            turn = 'Min'
        else:
            # Min plays greedily
            if cards[left] <= cards[right]:
                chosen = cards[left]
                left += 1
            else:
                chosen = cards[right]
                right -= 1
            min_score += chosen
            print(f"Min picks {chosen}, Remaining Cards: {cards[left:right+1]}")
            turn = 'Max'

    print(f"\nFinal Scores => Max: {max_score}, Min: {min_score}")
    winner = "Max" if max_score > min_score else "Min"
    print(f"Winner: {winner}")


# Example usage
cards = [14, 10, 6, 2, 9, 5]
play_game(cards)
