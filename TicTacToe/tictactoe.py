import random

# Визначаємо розмір ігрового поля
SIZE = 3

# Створюємо ігрове поле
board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

# Визначаємо гравців
players = ['X', 'O']

# Визначаємо хід гравців
current_player = random.choice(players)

# Функція виведення ігрового поля
def print_board(board):
    for row in board:
        print(' | '.join(row))

# Функція отримання ходу гравця
def get_move(player):
    while True:
        move = input(f'Ход гравця {player}: ')
        move = move.split(' ')
        if len(move) != 2:
            print('Неправильний формат ходу.')
            continue
        try:
            move = [int(m) for m in move]
        except ValueError:
            print('Неправильний формат ходу.')
            continue
        if 0 <= move[0] < SIZE and 0 <= move[1] < SIZE and board[move[0]][move[1]] == ' ':
            return move
        print('Клітинка зайнята.')

# Цикл гри
while True:
    # Виводимо ігрове поле
    print_board(board)

    # Просимо гравця зробити хід
    move = get_move(current_player)

    # Перевіряємо, чи змінна move дорівнює None
    if move is None:
        print('Неправильний формат ходу.')
        continue

    # Ставимо фігуру гравця на ігрове поле
    board[move[0]][move[1]] = current_player


    def check_win(board, player):
        ...
    # Перевіряємо перемогу
    if check_win(board, current_player):
        print(f'Переміг гравець {current_player}')
        break

    # Змінюємо хід гравця
    current_player = players[players.index(current_player) ^ 1]