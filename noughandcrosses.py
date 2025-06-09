import random
import os.path
random.seed()

def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print('-' * (len(row) * 4 - 1))

def welcome(board):
    print("Welcome to the unbeatable noughts and crosses game")
    draw_board(board)

def initialise_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = ' '
    return board# After all the cell have been intialise the board return

    
def get_player_move(board):
    while True:
        try:
            row = int(input("Enter the row number (0, 1, or 2): "))
            col = int(input("Enter the column number (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col#If the move is valid, function returns the row and column as a tuple
            else:
                print("Invalid cell. Please choose an empty cell within the range (0, 1, 2).")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")

def choose_computer_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':#condition checks if the cell at the row-th row and col-th column is empty
                return row, col

def check_for_win(board, mark):

    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)): 
            # checks if all elements in the i-th row are equal to mark
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        #checks if all elements in the anti-diagonal  are equal to mark.
        return True
    return False

def check_for_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game(board):
    initialise_board(board)
    draw_board(board)
    
    while True:
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            return 1
        if check_for_draw(board):
            return 0
        
        comp_row, comp_col = choose_computer_move(board)
        board[comp_row][comp_col] = 'O'#place computer mark o
        draw_board(board)#computer move after display
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return 0

def menu():
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from the 'leaderboard.txt'")
    print("q - End the program")
    return input("Enter your choice: ")

def load_scores():
    leaders = {}
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            for line in file:
                player, score = line.strip().split(',')
                leaders[player] = int(score)
    return leaders

def save_score(score):
    name = input("Please enter your name: ")
    with open('leaderboard.txt', 'a') as file:
        file.write(f"{name},{score}\n")

def display_leaderboard(leaders):#that takes a dictionary leaders as input.
    print("Leaderboard:")
    print("Player:Score")
    for player, score in leaders.items():
        print(f"{player} : {score}")

def main():
    """Main function to run the menu and handle user choices."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        choice = menu() # return users choice
        if choice == '1':
            score = play_game(board)
        elif choice == '2': 
            save_score(score)
        elif choice == '3':
            leaders = load_scores()
            display_leaderboard(leaders)
        elif choice == 'q':
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__": # t's a conditional statement that executes a block of code only if the script is run directly, not imported as a module.
    main()