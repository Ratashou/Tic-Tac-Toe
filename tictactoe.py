#! python3
#A program to make a simple tic tac toe/noughts and crosses game

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '} #the different positions on the board

def printBoard(ticSpace):
    print(ticSpace['top-L'] + '|' + ticSpace['top-M'] + '|' + ticSpace['top-R'])
    print('-+-+-')
    print(ticSpace['mid-L'] + '|' + ticSpace['mid-M'] + '|' + ticSpace['mid-R'])
    print('-+-+-')
    print(ticSpace['bot-L'] + '|' + ticSpace['bot-M'] + '|' + ticSpace['bot-R']) #this function prints out a n+c board

printBoard(theBoard)

print('Who is going first? X or O?')
turn = input()
while turn != 'X' and turn!= 'O': #for an incorrect input
    print('A correct value wasn''t entered')
    print('Please enter either X or O to determine which piece will go first')
    turn = input()
usedMoves = [] #a list to check whether a selected move has been chosen already or not
for i in range(9): #for all 9 positions on the board
    print ('Choose a position to place an ' + turn + '''
    top-L (for top left)
    top-M (top middle)
    top-R (top right)
    mid-L (middle left)
    mid-M (the middle)
    mid-R (middle right)
    bot-L (bottom left)
    bot-M (bottom middle)
    bot-R (bottom right)''')

    move = input()
    while move in usedMoves:
        print('This position has already been chosen, choose another')
        move = input()
    usedMoves.append(move)
    theBoard[move] = turn #this takes the piece (X or O) currently playing and places it in the inputted position
    printBoard(theBoard)
    
    if (theBoard['top-L'] == turn and theBoard['top-M'] == turn and theBoard['top-R'] == turn) or \
       (theBoard['mid-L'] == turn and theBoard['mid-M'] == turn and theBoard['mid-R'] == turn) or \
       (theBoard['bot-L'] == turn and theBoard['bot-M'] == turn and theBoard['bot-R'] == turn) or \
       (theBoard['top-L'] == turn and theBoard['mid-L'] == turn and theBoard['bot-L'] == turn) or \
       (theBoard['top-M'] == turn and theBoard['mid-M'] == turn and theBoard['bot-M'] == turn) or \
       (theBoard['top-R'] == turn and theBoard['mid-R'] == turn and theBoard['bot-R'] == turn) or \
       (theBoard['top-L'] == turn and theBoard['mid-M'] == turn and theBoard['bot-R'] == turn) or \
       (theBoard['top-R'] == turn and theBoard['mid-M'] == turn and theBoard['bot-L'] == turn):
        win = 1
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    win = 0

if win == 1:
    print('Congratulations! ' + turn + ' wins!')

else:
    print('No one wins!')

