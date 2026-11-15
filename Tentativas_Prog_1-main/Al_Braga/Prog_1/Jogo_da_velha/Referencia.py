""""
-Matriz 3x3(lista de listas)
-Função que lê tabuleiro e guarde na memória
"""
import random
def displayBoard(board):
    print(" ", board[0], " | ", board[1], " | ", board[2])
    print("--------------------")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print("--------------------")
    print(" ", board[6], " | ", board[7], " | ", board[8])

def playerTurn(board):

    playerFlag = True

    while playerFlag == True:

        turn = int(input('Digite o numero da posição: '))

        playerFlag = False

        if board[turn - 1] != ' ':
            playerFlag = True
            print ('Valor inválido')

        board[turn - 1] = 'X'
        displayBoard(board)
        return board
def checkWinner(board, player):

    if (board[0] == player and board[1] == player and board[2] == player): #__
        print(player, ' é o ganhador!!!')
        return True
    elif (board[3] == player and board[4] == player and board[5] == player): # __
        print(player, ' é o ganhador!!!')
        return True
    elif (board[6] == player and board[7] == player and board[8] == player):#  __
        print(player, ' é o ganhador!!!')
        return True
    elif (board[0] == player and board[3] == player and board[6] == player):#|
        print(player, ' é o ganhador!!!')
        return True
    elif (board[1] == player and board[4] == player and board[7] == player):#|
        print(player, ' é o ganhador!!!')
        return True
    elif (board[2] == player and board[5] == player and board[8] == player):#|
        print(player, ' é o ganhador!!!')
        return True
    elif (board[2] == player and board[4] == player and board[6] == player):
        print(player, ' é o ganhador!!!')
        return True
    else:
        return False





def computerTurn(board):

    compFlag = True

    while compFlag == True:

        turn = int(random.randint(0, 8))


        if board[turn] == ' ':
            compFlag = False

    board[turn] = 'O'
    displayBoard(board)
    return board


def main( ) :
    board = [' '] * 9



    endgame = False
    turnCount = 0
    while endgame != True:
        displayBoard(board)

        board = playerTurn(board)
        turnCount += 1

        endgame = checkWinner(board, 'X')

        if endgame == False and turnCount != 9:
            board = computerTurn(board)
            turnCount += 1
            endgame = checkWinner(board, 'O')

        if turnCount == 9 and endgame == False:
            print('Sem ganhador!')
            endgame = True

if __name__ == "__main__":
    main( )