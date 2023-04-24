theBoard = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
def printBoard(board):
    print("\t\t", board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\t\t - + - + - ')
    print("\t\t", board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('\t\t - + - + - ')
    print("\t\t", board[7] + ' | ' + board[8] + ' | ' + board[9])
print("-----WELLCOME TO TIC TAC TOE MULTIPLAYER-----")
turn = 'X'
for _ in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = int(input())
    if theBoard[move]==' ':
        theBoard[move] = turn
    else:
        print('place already euipde ')
        continue

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
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'