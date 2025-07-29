from IPython.display import clear_output

def draw_board(board):
    clear_output()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def select_player():
    player1 = 'Wrong'
    while player1 not in ['X', 'O']:
        player1 = input("Player 1, choose your marker (X or O): ").upper()
        if player1 not in ['X', 'O']:
            print("Invalid, choose either 'X' or 'O'.")
        if player1 in ['X', 'O']:
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
    return (player1, player2)

def place_marker(board, marker):
    position = -1
    while position not in range(9):
        position = input(f"Player {marker}, choose your position (0-8): ")
        if not position.isdigit():
            print("Invalid input. Please enter a number between 0 and 8.")
            position = -1
        elif int(position) not in range(9):
            print("Invalid position. Choose a number between 0 and 8.")
            position = -1
        else:
            if board[int(position)] not in ['X', 'O']:
                board[int(position)] = marker
                return board
            else:
                print("Position already taken. Choose another position.")
                position = -1

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] == 'X':
            return 'X'
        elif board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] == 'O':
            return 'O'
    return 'F'
def main():
    #Welcome message
    print("Welcome to Tic Tac Toe!")

    #Select players
    player1, player2 = select_player()
    current_player = player1

    #Initialize the board
    board = [_ for _ in range(9)]
    draw_board(board)

    game_on = True
    while game_on:
        board = place_marker(board, current_player)
        draw_board(board)
        winner = check_winner(board)
        if winner != 'F':
            print(f"Player {winner} wins!")
            game_on = False
        current_player = player2 if current_player == player1 else player1


main()