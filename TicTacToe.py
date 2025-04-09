import math

# Initialize the board with underscores
board = ["_" for _ in range(9)]

# Display the board
def print_board():
    for i in range(0, 9, 3):
        print(" " + " ".join(board[i:i+3]))

# Check if the board is full
def is_board_full():
    return "_" not in board

# Check if a player has won
def check_winner(player):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == player for i in combo) for combo in wins)

# Minimax algorithm
def minimax(is_maximizing, alpha=-math.inf, beta=math.inf):
    if check_winner("X"): return -1
    if check_winner("O"): return 1
    if is_board_full(): return 0

    best_score = -math.inf if is_maximizing else math.inf
    player = "O" if is_maximizing else "X"
    for i in [i for i, x in enumerate(board) if x == "_"]:
        board[i] = player
        score = minimax(not is_maximizing, alpha, beta)
        board[i] = "_"
        if is_maximizing:
            best_score = max(best_score, score)
            alpha = max(alpha, score)
        else:
            best_score = min(best_score, score)
            beta = min(beta, score)
        if beta <= alpha:
            break
    return best_score

# Find the best move for AI
def best_move():
    best_score, move = -math.inf, None
    for i in [i for i, x in enumerate(board) if x == "_"]:
        board[i] = "O"
        score = minimax(False)
        board[i] = "_"
        if score > best_score:
            best_score, move = score, i
    return move

# Play the game
def play_game():
    print("Hi, this is a Tic Tac Toe game; please choose a position to place an 'X' on the following board\n")
    print_board()

    while True:
        try:
            # Player's move
            player_move = int(input("\nEnter your move (1-9): ")) - 1
            if board[player_move] != "_":
                print("Invalid move! Try again.")
                continue
            board[player_move] = "X"
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        print("\nEnd of the first round：")
        print_board()

        if check_winner("X"):
            print("You win!")
            break
        elif is_board_full():
            print("It's a draw!")
            break

        # AI's move
        board[best_move()] = "O"
        print("\nEnd of the first round：")
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        elif is_board_full():
            print("It's a draw!")
            break

# Start the game
play_game()
