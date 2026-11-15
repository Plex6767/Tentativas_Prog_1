import random
def displayBoard(board):
    print(" ", board[0][0], " | ", board[0][1], " | ", board[0][2])
    print("------------------")
    print(" ", board[1][0], " | ", board[1][1], " | ", board[1][2])
    print("------------------")
    print(" ", board[2][0], " | ", board[2][1], " | ", board[2][2])


def checkWinner(board, player):
    # Linhas horizontais
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    # Colunas verticais
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    # Diagonais
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def limpar_tela():
    print("\033[H\033[J", end="")


def main():
    board = [[' '] * 3 for _ in range(3)]
    n = 1

    while True:
        limpar_tela()
        displayBoard(board)
        current_player = 'X' if n % 2 != 0 else 'O'
        x = input(f"\nPlayer {current_player}, enter position (1-9): ").strip()
        match x:
            case "1" if board[0][0] == " ":
                board[0][0] = current_player
            case "2" if board[0][1] == " ":
                board[0][1] = current_player
            case "3" if board[0][2] == " ":
                board[0][2] = current_player
            case "4" if board[1][0] == " ":
                board[1][0] = current_player
            case "5" if board[1][1] == " ":
                board[1][1] = current_player
            case "6" if board[1][2] == " ":
                board[1][2] = current_player
            case "7" if board[2][0] == " ":
                board[2][0] = current_player
            case "8" if board[2][1] == " ":
                board[2][1] = current_player
            case "9" if board[2][2] == " ":
                board[2][2] = current_player
            case _:
                input("Posição inválida ou já ocupada! Pressione Enter para tentar novamente...")
                continue

        if checkWinner(board, current_player):
            limpar_tela()
            displayBoard(board)
            print(f"\n{current_player} é o ganhador!!!")
            break

        if n == 9:
            limpar_tela()
            displayBoard(board)
            print("\nDeu velha! Empate!")
            break

        n += 1


if __name__ == "__main__":
    main()