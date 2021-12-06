import re

MAX_COORDINATE = 1000
# False - part 1, True - part 2
CONSIDER_DIAGONALS = True

LINE_REGEX = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

grid = [[0] * MAX_COORDINATE for _ in range(MAX_COORDINATE)]

with open("input.txt", "r") as input_file:
    for line in input_file.readlines():
        x1, y1, x2, y2 = [int(num) for num in LINE_REGEX.search(line).groups()]
        if x1 == x2:
            y_from = min(y1, y2)
            y_to = max(y1, y2)
            for y in range(y_from, y_to + 1):
                grid[x1][y] += 1
        elif y1 == y2:
            x_from = min(x1, x2)
            x_to = max(x1, x2)
            for x in range(x_from, x_to + 1):
                grid[x][y1] += 1
        elif CONSIDER_DIAGONALS:
            x = x1
            y = y1
            while True:
                grid[x][y] += 1
                if x == x2 and y == y2:
                    break
                x = x + 1 if x < x2 else x - 1
                y = y + 1 if y < y2 else y - 1

total = 0

for x in range(MAX_COORDINATE):
    for y in range(MAX_COORDINATE):
        if grid[x][y] > 1:
            total += 1

print(total)
