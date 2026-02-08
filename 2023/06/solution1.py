file = open("input.txt", "r")
lines = file.read().splitlines()

times = [int(x) for x in lines[0].split(' ')[1:] if x.strip() != '']
distances = [int(x) for x in lines[1].split(' ')[1:] if x.strip() != '']

def calculate_distance(speed, time):
    return speed * time

def calculate_competitive_solutions(total_time, distance_to_beat):
    competitive_solutions = 0
    for speed in range(total_time):
        time_remaining = total_time - speed
        if calculate_distance(speed, time_remaining) > distance_to_beat:
            competitive_solutions += 1
    return competitive_solutions

competitive_solutions = [calculate_competitive_solutions(times[idx], distances[idx]) for idx in range(len(times))]

total_competitive_solutions = 1
for competitive_solution in competitive_solutions:
    total_competitive_solutions *= competitive_solution
print(total_competitive_solutions)