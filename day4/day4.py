SIZE = 5


class Board:

    def __init__(self, rows):
        self.unmarked_numbers_by_row = [set(row) for row in rows]
        self.unmarked_numbers_by_column = []
        self.won = False

        for i in range(SIZE):
            column = set([row[i] for row in rows])
            self.unmarked_numbers_by_column.append(column)

    def mark_and_check_victory(self, number):
        for line in self.unmarked_numbers_by_column + self.unmarked_numbers_by_row:
            line.discard(number)
            if len(line) == 0:
                self.won = True
        return self.won

    def calculate_score(self, last_number):
        return last_number * \
            sum([number for row in self.unmarked_numbers_by_row for number in row])


numbers = []
boards = []

with open("input.txt", "r") as input_file:
    numbers = [int(number) for number in input_file.readline().split(',')]

    while line := input_file.readline():
        rows = [list(map(lambda value: int(value), line.split()))
                for line in [input_file.readline() for _ in range(SIZE)]]
        boards.append(Board(rows))

# first printed number is the answer to part 1
# last printed number is the answer to part 2
for number in numbers:
    for board in boards:
        if board.won:
            continue
        if board.mark_and_check_victory(number):
            print(board.calculate_score(number))
