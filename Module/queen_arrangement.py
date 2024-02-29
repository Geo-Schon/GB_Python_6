import random


def random_queens_arrangement():
    while True:
        queens_positions = [(i, random.randint(1, 8)) for i in range(1, 9)]
        return queens_positions


def test_random_arrangements(num_tests=4):
    successful_arrangements = []
    for _ in range(num_tests):
        arrangement = random_queens_arrangement()
        successful_arrangements.append(arrangement)
    return successful_arrangements


def print_chessboard(arrangement):
    for i in range(1, 9):
        row = ['Q' if (i, j) in arrangement else '.' for j in range(1, 9)]
        print(' '.join(row))
