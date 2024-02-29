import random


def arrangement():
    all_the_lst = []
    while len(all_the_lst) < 8:
        i = random.randint(1, 8)
        j = random.randint(1, 8)
        two = [i, j]
        if two not in all_the_lst:
            all_the_lst += [two]
        lines = []
        columns = []
        for pair in all_the_lst:
            i, j = pair
            lines.append(i)
            columns.append(j)
        if len(set(lines)) != len(lines) or len(set(columns)) != len(columns):
            all_the_lst.pop()
            continue
    yield all_the_lst


def chess_board(lst: list[list], num=8):
    board = [[' ::' for _ in range(num)] for _ in range(num)]
    for coordinates in lst:
        x, y = coordinates
        board[x - 1][y - 1] = ' ' + chr(9813)
    for row in board:
        print(' '.join(row))
    return '\n\n'


def queen_beats_checking(lst: list[list]):
    for two in lst:
        a, b = two
        i = a
        j = b
        gen = ([i, j] for i, j in zip(range(i - 1, 0, -1), range(j - 1, 0, -1)))
        for x, y in gen:
            if [x, y] in lst:
                return False
        gen = ([i, j] for i, j in zip(range(i + 1, 9), range(j + 1, 9)))
        for x, y in gen:
            if [x, y] in lst:
                return False
        gen = ([i, j] for i, j in zip(range(i - 1, 0, -1), range(j + 1, 9)))
        for x, y in gen:
            if [x, y] in lst:
                return False
        gen = ([i, j] for i, j in zip(range(i + 1, 9), range(j - 1, 0, -1)))
        for x, y in gen:
            if [x, y] in lst:
                return False
    return True


def winner_num_combinations(num: int):
    win_combinations = []
    while True:
        ar = next(arrangement())
        if queen_beats_checking(ar):
            win_combinations.append(ar)
        if len(win_combinations) == num:
            return win_combinations


if __name__ == '__main__':
    for choice in winner_num_combinations(4):
        print(choice)
        print(chess_board(choice))
