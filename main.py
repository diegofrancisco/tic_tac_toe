import random


def clear_output():
    print('\n' * 100)


def display_board(board):
    drawnboard = '\n'
    for index, entry in enumerate(board):
        if index == 0: continue
        drawnboard += f'\t{entry}\t'
        if index % 3 == 0:
            drawnboard += '\n'
        else:
            drawnboard += '|'
    print(drawnboard)


def player_input():
    choosenmarker = ''
    while choosenmarker == '':
        entrada = input('Escolha qual será o seu simbolo: X ou O')
        if entrada == 'X' or entrada == 'O':
            choosenmarker = entrada
            print(f'Você escolheu o marcador {choosenmarker}')
        else:
            print('Símbolo inválido!!')
    return choosenmarker


def place_marker(board, marker, position):
    if (position == 7):
        board[1] = marker
    elif (position == 8):
        board[2] = marker
    elif (position == 9):
        board[3] = marker
    elif (position == 4):
        board[4] = marker
    elif (position == 5):
        board[5] = marker
    elif (position == 6):
        board[6] = marker
    elif (position == 1):
        board[7] = marker
    elif (position == 2):
        board[8] = marker
    elif (position == 3):
        board[9] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # horizontal-topo
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # horizontal-meio
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # horizontal-baixo
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # vertical-esquerda
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # vertical-meio
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # vertical-direita
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    return f'Jogador {random.randint(1, 2)} vai primeiro!!'


def space_check(board, position):
    if(position == 7): return board[1] == ' '
    elif(position == 8): return board[2] == ' '
    elif(position == 9): return board[3] == ' '
    elif(position == 4): return board[4] == ' '
    elif(position == 5): return board[5] == ' '
    elif(position == 6): return board[6] == ' '
    elif(position == 1): return board[7] == ' '
    elif(position == 2): return board[8] == ' '
    elif(position == 3): return board[9] == ' '


def full_board_check(board):
    boardIsFull = True
    for entry in board:
        if(entry == ' '):
            boardIsFull = False
            break
    return boardIsFull


def player_choice(board, turn):
    posicao = -1
    while(posicao == -1):
        escolha = int(input(turn + ', qual a posição da sua próxima jogada?'))
        if(escolha in range(1,10)):
            if(space_check(board, escolha)):
                posicao = escolha
            else:
                print('Posição escolhida não está vazia!')
        else:
            print('Posição inválida!')
    return posicao


def replay():
    return input('Você quer jogar novamente? ("Y" ou "N")') == 'Y'


if __name__ == "__main__":
    print('Bem vindo ao Tic Tac Toe!')
    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker = player_input()
        player2_marker = 'X'
        if (player1_marker == 'X'): player2_marker = 'O'
        turn = choose_first()
        print(turn + ' vai primeiro!')

        play_game = input('Você está pronto para jogar? ("S" ou "N")')

        if play_game.lower()[0] == 's':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Jogador 1':
                # Player1's turn.

                display_board(theBoard)
                position = player_choice(theBoard, turn)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Jogador 1 ganhou!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('Empate =/')
                        break
                    else:
                        turn = 'Jogador 2'

            else:
                # Player2's turn.

                display_board(theBoard)
                position = player_choice(theBoard, turn)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Jogador 2 ganhou!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('Empate =/')
                        break
                    else:
                        turn = 'Jogador 1'

        if not replay():
            break