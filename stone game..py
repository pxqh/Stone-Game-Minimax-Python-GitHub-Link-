def minimax(stones, is_maximizing):
    if stones == 0:
        return -1 if is_maximizing else 1

    if is_maximizing:
        best_score = -float('inf')
        for move in [1, 2]:
            if stones >= move:
                score = minimax(stones - move, False)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in [1, 2]:
            if stones >= move:
                score = minimax(stones - move, True)
                best_score = min(best_score, score)
        return best_score

def best_move(stones):
    move = None
    best_score = -float('inf')
    for m in [1, 2]:
        if stones >= m:
            score = minimax(stones - m, False)
            if score > best_score:
                best_score = score
                move = m
    return move

def play_game():
    stones = int(input("Enter the number of stones: "))
    while stones > 0:
        print(f"Stones left: {stones}")
        ai_move = best_move(stones)
        print(f"AI removes {ai_move} stones")
        stones -= ai_move
        if stones == 0:
            print("AI wins!")
            break
        player_move = int(input("Your turn! Remove 1 or 2 stones: "))
        stones -= player_move
        if stones == 0:
            print("You win!")

if __name__ == "__main__":
    play_game()
