import heapq

file = open("input.txt", "r")
lines = file.read().splitlines()

coordinates = [[int(x_str) for x_str in line.split(",")] for line in lines]
distances = []

for i in range(len(coordinates)):
    for j in range(i):
        x1, y1, z1 = coordinates[i]
        x2, y2, z2 = coordinates[j]
        distance_sq = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1)
        heapq.heappush(distances, (distance_sq, i, j))

orphaned_circuits = set([i for i in range(len(coordinates))])
circuit_ids = {}
circuits = {}

last_i = -1
last_j = -1

while (len(orphaned_circuits) > 0 or len(circuits) != 1) and len(distances) > 0:
    (_, i, j) = heapq.heappop(distances)
    circuit = {i, j}

    if i in circuit_ids:
        circuit.update(circuits[circuit_ids[i]])
        del circuits[circuit_ids[i]]
    if j in circuit_ids and circuit_ids[j] in circuits:
        circuit.update(circuits[circuit_ids[j]])
        del circuits[circuit_ids[j]]

    for node in circuit:
        circuit_ids[node] = i
        if node in orphaned_circuits:
            orphaned_circuits.remove(node)
    circuits[i] = circuit

    last_i = i
    last_j = j

print("Last merged nodes: (%d, %d, %d) and (%d, %d, %d)" % (coordinates[last_i][0], coordinates[last_i][1], coordinates[last_i][2], coordinates[last_j][0], coordinates[last_j][1], coordinates[last_j][2]))
print("Multiplication of the X coordinates: %d" % (coordinates[last_i][0] * coordinates[last_j][0]))
