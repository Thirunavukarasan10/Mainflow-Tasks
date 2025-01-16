import math

board = [' ' for _ in range(9)]
def display_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("-" * 5)
    print("\n")
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
def get_available_moves():
    return [i for i in range(9) if board[i] == ' ']
def minimax(is_maximizing):
    if check_winner('O'):
        return 1  # AI wins
    if check_winner('X'):
        return -1  # Player wins
    if ' ' not in board:
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves():
            board[move] = 'O'
            score = minimax(False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves():
            board[move] = 'X'
            score = minimax(True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score
def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves():
        board[move] = 'O'
        score = minimax(False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
def play_game():
    user_turn = True
    while True:
        display_board()
        if user_turn:
            try:
                move = int(input("Enter your move (0-8): "))
                if board[move] == ' ':
                    board[move] = 'X'
                    if check_winner('X'):
                        display_board()
                        print("You win!")
                        break
                    user_turn = False
                else:
                    print("Invalid move! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter a number between 0 and 8.")
        else:
            print("AI is making its move...")
            move = ai_move()
            board[move] = 'O'
            if check_winner('O'):
                display_board()
                print("AI wins!")
                break
            user_turn = True

        if ' ' not in board:
            display_board()
            print("It's a draw!")
            break
play_game()
