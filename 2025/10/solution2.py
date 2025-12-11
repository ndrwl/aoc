file = open("input.txt", "r")
lines = file.read().splitlines()

def parse_line_as_ilp(line):
    move_strs = [move_str[1:-1] for move_str in line[line.index(']') + 1:line.index('{')-1].strip().split(' ')]
    goal_str = line[line.index('{')+1:line.index('}')]

    goal = [int(num_str) for num_str in goal_str.split(',')]
    moves = []
    for move_str in move_strs:
        move = [0] * len(goal)
        for pos_str in move_str.split(','):
            pos = int(pos_str)
            move[pos] = 1
        moves.append(move)

    ilp_matrix = [[moves[j][i] for j in range(len(moves))] + [goal[i]] for i in range(len(goal))]
    return ilp_matrix

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gaussian_elimination(matrix):
    for row in range(len(matrix)):
        # pivot on the first column in this row
        pivot_col = next(iter(col for col in range(len(matrix[row]) - 1) if matrix[row][col] != 0), None)

        if pivot_col is None:
            continue

        if matrix[row][pivot_col] < 0:
            for c in range(len(matrix[row])):
                matrix[row][c] *= -1

        for r in range(len(matrix)):
            if r == row:
                continue
            if matrix[r][pivot_col] == 0:
                continue

            pivot_gcd = gcd(matrix[r][pivot_col], matrix[row][pivot_col])
            multiple = matrix[row][pivot_col] // pivot_gcd
            factor = matrix[r][pivot_col] // pivot_gcd

            for c in range(len(matrix[r])):
                matrix[r][c] *= multiple
                matrix[r][c] -= factor * matrix[row][c]

    matrix[:] = [row for row in matrix if any(val != 0 for val in row)]

def solve_pivots(matrix, pivot_columns, free_columns, free_values):
    solution = [0] * (len(pivot_columns) + len(free_columns))
    for i in range(len(free_columns)):
        solution[free_columns[i]] = free_values[i]

    for row in range(len(matrix)):
        pivot_col = pivot_columns[row]
        pivot_factor = matrix[row][pivot_col]

        sum_free = sum(matrix[row][free_col] * solution[free_col] for free_col in free_columns)
        sol = matrix[row][-1] - sum_free

        if sol % pivot_factor != 0 or sol < 0:
            return None

        solution[pivot_col] = sol // pivot_factor

    return sum(solution)

def brute_force_free_variables_internal(matrix, max_goal, pivot_columns, free_columns, free_values):
    if len(free_values) < len(free_columns):
        min_solution = None
        for val in range(max_goal):
            solution = brute_force_free_variables_internal(matrix, max_goal, pivot_columns, free_columns, free_values + [val])
            if solution is not None:
                if min_solution is None or solution < min_solution:
                    min_solution = solution
                    # Reduce max_goal to current min_solution sum to prune search space
                    max_goal = min_solution
        return min_solution

    return solve_pivots(matrix, pivot_columns, free_columns,free_values)

def brute_force_free_variables(matrix, max_goal):
    pivot_columns = [next(col for col in range(len(matrix[row])) if matrix[row][col] != 0) for row in range(len(matrix))]
    free_columns = [col for col in range(len(matrix[0]) - 1) if col not in pivot_columns]

    return brute_force_free_variables_internal(matrix, max_goal, pivot_columns, free_columns, [])

def solve_ilp(matrix):
    max_goal = max([row[-1] for row in matrix])
    gaussian_elimination(matrix)
    solution = brute_force_free_variables(matrix, max_goal)
    return solution

total_moves = 0
for line in lines:
    matrix = parse_line_as_ilp(line)
    total_moves += solve_ilp(matrix)

print("Total moves: %d" % total_moves)