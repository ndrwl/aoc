file = open("input.txt", "r")
board = file.read().splitlines()

def find_start(board):
    for x, line in enumerate(board):
        for y, char in enumerate(line):
            if char == "S":
                return x, y

def explore_path(board, fill_board, start_x, start_y, x, y):
    prev_x, prev_y = start_x, start_y
    length = 1

    while length == 1 or not (x == start_x and y == start_y):
        # explore
        candidates = []
        match board[x][y]:
            case "|":
                candidates.append((1, 0))
                candidates.append((-1, 0))
            case "-":
                candidates.append((0, 1))
                candidates.append((0, -1))
            case "L":
                candidates.append((-1, 0))
                candidates.append((0, 1))
            case "J":
                candidates.append((-1, 0))
                candidates.append((0, -1))
            case "7":
                candidates.append((1, 0))
                candidates.append((0, -1))
            case "F":
                candidates.append((1, 0))
                candidates.append((0, 1))

        if (len(candidates) != 2):
            return False, 0

        chosen = (0,0)

        length += 1;
        if (candidates[0] == (prev_x - x, prev_y - y)):
            chosen = candidates[1]
        elif (candidates[1] == (prev_x - x, prev_y - y)):
            chosen = candidates[0]
        else:
            return False, 0

        fill_board[x * 2 + chosen[0]    ][y * 2 + chosen[1]    ] = 1
        fill_board[x * 2 + chosen[0] * 2][y * 2 + chosen[1] * 2] = 1

        prev_x, prev_y = x, y
        x += chosen[0]
        y += chosen[1]

    return True, length

def flood_fill(fill_board):

    rows = len(fill_board)
    columns = len(fill_board[0])

    filled = True
    while (filled):
        filled = False

        for x in range(2, rows - 1):
            for y in range(2, columns - 1):
                if (fill_board[x][y] != 0):
                    continue

                if (fill_board[x - 1][y] == 2 or fill_board[x + 1][y] == 2 or fill_board[x][y - 1] == 2 or fill_board[x][y + 1] == 2):
                    fill_board[x][y] = 2
                    filled = True


def fill_edges(fill_board):
    for y in range(len(fill_board[0])):
        if (fill_board[0][y] == 0):
            fill_board[0][y] = 2
        if (fill_board[len(fill_board) - 1][y] == 0):
            fill_board[len(fill_board) - 1][y] = 2

    for x in range(len(fill_board)):
        if (fill_board[x][0] == 0):
            fill_board[x][0] = 2
        if (fill_board[x][len(fill_board[0]) - 1] == 0):
            fill_board[x][len(fill_board[0]) - 1] = 2

def count_unfilled(fill_board):
    count = 0
    for x, row in enumerate(fill_board):
        for y, piece in enumerate(row):
            if (piece == 0 and x % 2 == 0 and y % 2 == 0):
                count += 1
    return count

start_x, start_y = find_start(board)

for dir_x, dir_y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

    fill_board = []
    for row in board:
        fill_board.append([0] * 2 * len(row))
        fill_board.append([0] * 2 * len(row))
    fill_board[start_x * 2][start_y * 2] = 1
    fill_board[start_x * 2 + dir_x    ][start_y * 2 + dir_y    ] = 1
    fill_board[start_x * 2 + dir_x * 2][start_y * 2 + dir_y * 2] = 1

    found, length = explore_path(board, fill_board, start_x, start_y, start_x + dir_x, start_y + dir_y)

    if (found):
        print(int((length + 1) / 2))
        fill_edges(fill_board)
        flood_fill(fill_board)
        print(count_unfilled(fill_board))
        break
