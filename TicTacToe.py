import random
import re
import sys
import numpy as np

GAME_ROLE = {'1', '2'}
UseAI = False
HumanFirst = True
DEBUG = 0

# board is a 2d array board[3][3]
def drawBoard(board):
    brd_copy = board.copy()
    
    print('==================')
    print('----------')
    for row in board:
        rowStr = '|' + '|'.join(['  ' if item != 0 else str(item) for item in row]) + '|'
        print(rowStr)
        print('----------')
    
def askStartGame():
    print('Do you want to start the game? (yes or no)')
    cmd = input().lower()
    if cmd == 'no':
        return False
    
    str = "Game Start!"
    print('Do you want to play with AI? (yes or no)')
    cmd = input().lower()
    if cmd == "yes":
        UseAI = True
        str += " Play with AI, and"
    else:
        UseAI = False
    
    print('Do you want to play first? (yes or no)')
    cmd = input().lower()
    if cmd == 'yes':
        HumanFirst = True
        str += " You are the First player."
    else:
        HumanFirst = False

    print(str)
    return True

def isComplete(board):
    return np.nonzero(board)
    
def askHumanNextMove(board):
    while True:
        print('Please enter your next move [row,col] :')
        move = input()
        match = re.match(r'[(\d),(\d)]', move);
        if match:
            row = int(match.group(1))
            col = int(match.group(2))
            if row > 0 and row < 4 and col > 0 and col < 4:
                if board[row-1][col-1] == '':
                    return row-1, col-1
                else:
                    print('The cell is already taken. Please try again.')
            else:
                print('Invalid input. Please try again.')
                
def botNextMove(board):
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if board[row][col] == '':
            return row, col
    
while (askStartGame() == True):
    board = np.zeros([3,3], dtype = 'str')
    drawBoard(board)

print('Goodbye!')
sys.exit()