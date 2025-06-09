import random #use the random number generator.
import os.path #handle file paths and check if files exist.

random.seed()#he random number generator with the current system time or another source of randomness.
# every time it will be different
def draw_board(board):
    for row in board:
        print(" | ".join(row))#joins each element into a single string, with " | " as the separator.
        #/use in vertical bar /separate the elements in the row
        print('-' * (len(row) * 4 - 1))# line of dashes to separate rows.
        #'-': This is a string containing a single dash.
        #*: This operator is used to repeat specified number of times
        #(len(row) * 4 - 1): This calculates the number of times to repeat the dash
        # *4-3 dashes between 4 slots (i.e., cells) in the row and 1 extra for spacing.
def welcome(board):
    print("Welcome to the unbeatable noughts and crosses game")
    draw_board(board)

def initialise_board(board):#(board): The function takes one argument, board, which is a list of lists representing the game board.
    for row in range(len(board)):#len(board): This returns the number of rows in the board.(o-1)
        for col in range(len(board[row])):#len(board[row]): This returns the number of columns in the current row.(0--1)
            board[row][col] = ' '#resetting the cell to be empty.
    return board# After all the cell have been intialise the board return


def get_player_move(board):
    while True:#continue to execute as long as the condition is True.
        try:
            row = int(input("Enter the row number (0, 1, or 2): "))
            #user enter row number as string and convert into integer by int
            col = int(input("Enter the column number (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
 #board[row][col] == ' ': This checks if the cell at the specified row and column is empty (contains a space character ' ').
                return row, col
#row, col:If the move is valid, function returns the row and column as a tuple
            else:
                #if condition is false
                print("Invalid cell. Please choose an empty cell within the range (0, 1, 2).")
        except ValueError:# handles exception occur in try /input canot converted into integer
            print("Invalid input. Please enter integers for row and column.")

def choose_computer_move(board):
#The function takes one argument, board, which is a list of lists representing the game board.
    for row in range(3):
        for col in range(3):#[0, 1, 2]the column indices of the board.
            if board[row][col] == ' ':#condition checks if the cell at the row-th row and col-th column is empty
                return row, col
#If an empty cell is found, the function returns the row and column indices as a tuple.


def check_for_win(board, mark):
   #board 3*3 list erpresent board
   #mark player symbol x and o
    for i in range(3):# sequence of numbers from 0 to 2 (3 is not included).
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            #== mark checks if the element in the board is equal to the mark.
            #all(board[i][j] == mark for j in range(3)) checks if all elements in the i-th row are equal to mark
                return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
#all(board[i][i] == mark for i in range(3)) checks if all elements in the main diagonal (from top-left to bottom-right) are equal to mark.
#all(board[i][2 - i] == mark for i in range(3)) checks if all elements in the anti-diagonal (from top-right to bottom-left) are equal to mark.
        return True# if all the element are equal
    return False# row.col,diagnol contain mark

def check_for_draw(board):
    return all(cell != ' ' for row in board for cell in row)
#all() is a function that returns True
#for row in board iterates over each row in the board
#for cell in row iterates over each cell in the current row.
#current cell is not equal to a space character 


def play_game(board):
    initialise_board(board)#set up the board with empty spaces 
    draw_board(board)# prints the current state of the board to the screen.
    
    while True:# return statement executed inside the loop
        player_row, player_col = get_player_move(board)#call fun, player move,return row col,player mark placex

        board[player_row][player_col] = 'X'
        draw_board(board)#update and display board after player move
        if check_for_win(board, 'X'):
            return 1#win player
        if check_for_draw(board):
            return 0#draw 
        
        comp_row, comp_col = choose_computer_move(board)##call fun, comp move,return row col,comp mark place o

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
    leaders = {}#This initializes an empty dictionary named leaders and store key as name of player and value as score.
    if os.path.exists('leaderboard.txt'):
#is a conditional check that ensures the program only tries to read the file if it actually exists, preventing errors that would occur if the file were missing.
        with open('leaderboard.txt', 'r') as file:#opens the file leaderboard.txt in read mode ('r').
            for line in file:#iterates over each line in the file.
                player, score = line.strip().split(',')#splits the line into two parts at the comma.
                leaders[player] = int(score)#adds an entry to the leaders dictionary with the player's name as the key and the score as the value.
    return leaders# return leader dictionary and contain player name and score from the file

def save_score(score):# which will hold the score to be saved.
    name = input("Please enter your name: ")
    with open('leaderboard.txt', 'a') as file:#open file in append mode
        file.write(f"{name},{score}\n")#write player name,score in file
#\n each entry is on a new line.

def display_leaderboard(leaders):#that takes a dictionary leaders as input.
    print("Leaderboard:")#indicate what will display next
    print("Player:Score")#first col represent playername and second score
    for player, score in leaders.items():#is a loop that iterates over each key-value pair in the leaders dictionary.
        print(f"{player}: {score}")# print player name and score seperate by colon and space


def main():
    """Main function to run the menu and handle user choices."""#doc string 
    board = [[' ' for _ in range(3)] for _ in range(3)]#creates a 3x3 grid in game board, filled empty space
    while True:
        choice = menu() # call fun, return users choice
        if choice == '1':
            score = play_game(board)#start a game.
        elif choice == '2': 
            save_score(score)#save score
        elif choice == '3':
            leaders = load_scores()#load leaderboard from file
            display_leaderboard(leaders)#display leaderboard to user
        elif choice == 'q':
            break#loop terminate
        else:
            print("Invalid choice! Please try again.") # user invalid choice, an error message and try again.

if __name__ == "__main__": #fun excute when python block is run directlyas main program rather then other imported moduled
    main() #to start program      