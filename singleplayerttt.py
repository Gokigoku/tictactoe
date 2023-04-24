import random
import time

theBoard = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
def printBoard(board):
    print("\t\t", board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\t\t - + - + - ')
    print("\t\t", board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('\t\t - + - + - ')
    print("\t\t", board[7] + ' | ' + board[8] + ' | ' + board[9])

print("-----WELLCOME TO TIC TAC TOE SINGLE PLAYER-----")
printBoard(theBoard)

flag = False
mv = 0
count = 0
ch = input("Select 'X' or 'O' :-\n")
if ch == 'X':
    move = 'O'
else:
    move = 'X'
while True:
    if flag == False:
        n = random.randint(1, 9)
        if theBoard[n] == ' ':
           theBoard[n] = str(move)
           print("\tComputer choice is ", n)
           printBoard(theBoard)
           if (theBoard[1] == 'X' and theBoard[5] == 'X' and theBoard[9] == 'X' or
                   theBoard[4] == 'X' and theBoard[5] == 'X' and theBoard[6] == 'X' or
                   theBoard[3] == 'X' and theBoard[5] == 'X' and theBoard[7] == 'X' or
                   theBoard[1] == 'X' and theBoard[2] == 'X' and theBoard[3] == 'X' or
                   theBoard[7] == 'X' and theBoard[8] == 'X' and theBoard[9] == 'X' or
                   theBoard[1] == 'X' and theBoard[4] == 'X' and theBoard[7] == 'X' or
                   theBoard[2] == 'X' and theBoard[5] == 'X' and theBoard[8] == 'X' or
                   theBoard[3] == 'X' and theBoard[6] == 'X' and theBoard[9] == 'X'):
               print("Player 'X' is the Winner")
               break
           if (theBoard[1] == 'O' and theBoard[5] == 'O' and theBoard[9] == 'O' or
                   theBoard[4] == 'O' and theBoard[5] == 'O' and theBoard[6] == 'O' or
                   theBoard[3] == 'O' and theBoard[5] == 'O' and theBoard[7] == 'O' or
                   theBoard[1] == 'O' and theBoard[2] == 'O' and theBoard[3] == 'O' or
                   theBoard[7] == 'O' and theBoard[8] == 'O' and theBoard[9] == 'O' or
                   theBoard[1] == 'O' and theBoard[4] == 'O' and theBoard[7] == 'O' or
                   theBoard[2] == 'O' and theBoard[5] == 'O' and theBoard[8] == 'O' or
                   theBoard[3] == 'O' and theBoard[6] == 'O' and theBoard[9] == 'O'):
               print("Player 'O' is the Winner")
               break
           count += 1
           if count == 9:
               break
        else:
           continue
    time.sleep(0.5)
    try:
        mv = int(input("\tEnter your choice :-\n"))
    except KeyError as k:
        print("\tInvalid Choice", k)
    except ValueError as v:
        print("\tInvalid input", v)
    if theBoard[mv] == ' ':
        theBoard[mv] = str(ch)
        flag = False
        printBoard(theBoard)
        if (theBoard[1] == 'X' and theBoard[5] == 'X' and theBoard[9] == 'X' or
                theBoard[4] == 'X' and theBoard[5] == 'X' and theBoard[6] == 'X' or
                theBoard[3] == 'X' and theBoard[5] == 'X' and theBoard[7] == 'X' or
                theBoard[1] == 'X' and theBoard[2] == 'X' and theBoard[3] == 'X' or
                theBoard[7] == 'X' and theBoard[8] == 'X' and theBoard[9] == 'X' or
                theBoard[1] == 'X' and theBoard[4] == 'X' and theBoard[7] == 'X' or
                theBoard[2] == 'X' and theBoard[5] == 'X' and theBoard[8] == 'X' or
                theBoard[3] == 'X' and theBoard[6] == 'X' and theBoard[9] == 'X'):
            print("Player 'X' is the Winner")
            break
        if (theBoard[1] == 'O' and theBoard[5] == 'O' and theBoard[9] == 'O' or
                theBoard[4] == 'O' and theBoard[5] == 'O' and theBoard[6] == 'O' or
                theBoard[3] == 'O' and theBoard[5] == 'O' and theBoard[7] == 'O' or
                theBoard[1] == 'O' and theBoard[2] == 'O' and theBoard[3] == 'O' or
                theBoard[7] == 'O' and theBoard[8] == 'O' and theBoard[9] == 'O' or
                theBoard[1] == 'O' and theBoard[4] == 'O' and theBoard[7] == 'O' or
                theBoard[2] == 'O' and theBoard[5] == 'O' and theBoard[8] == 'O' or
                theBoard[3] == 'O' and theBoard[6] == 'O' and theBoard[9] == 'O'):
            print("Player 'O' is the Winner")
            break
        count += 1
        if count == 9:
            break
    else:
        print("Place already equipped")
        flag = True
        continue





