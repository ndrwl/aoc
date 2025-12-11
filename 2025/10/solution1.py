file = open("input.txt", "r")
lines = file.read().splitlines()

def parse_line(line):
    goal_str = line[1:line.index(']')]
    move_strs = [move_str[1:-1] for move_str in line[line.index(']') + 1:line.index('{')-1].strip().split(' ')]

    goal = sum([1 << idx for idx, char in enumerate(goal_str) if char == '#'])
    moves = [sum(1 << int(pos_str) for pos_str in move_str.split(',')) for move_str in move_strs]
    return goal, moves

def bfs_solve(goal, moves):
    visited = {}
    queue = [0]
    move_count = 1

    while queue:
        new_queue = []
        for state in queue:
            for move in moves:
                new_state = state ^ move
                if new_state == goal:
                    return move_count
                if new_state not in visited:
                    visited[new_state] = True
                    new_queue.append(new_state)
        move_count += 1
        queue = new_queue
    return -1

total_moves = 0
for line in lines:
    goal, moves = parse_line(line)
    total_moves += bfs_solve(goal, moves)

print("Total moves: %d" % total_moves)