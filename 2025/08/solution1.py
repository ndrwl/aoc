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
        distances.append((distance_sq, i, j))

circuit_ids = {}
circuits = {}

distances_to_merge = [(i, j) for (_, i, j) in heapq.nsmallest(1000, distances)]

for (i, j) in distances_to_merge:
    circuit = {i, j}

    if i in circuit_ids:
        circuit.update(circuits[circuit_ids[i]])
        del circuits[circuit_ids[i]]
    if j in circuit_ids and circuit_ids[j] in circuits:
        circuit.update(circuits[circuit_ids[j]])
        del circuits[circuit_ids[j]]

    for node in circuit:
        circuit_ids[node] = i
    circuits[i] = circuit

largest_circuits = heapq.nlargest(3, [len(circuit) for circuit in circuits.values()])
print("Product of sizes of three largest circuits: %d" % (largest_circuits[0] * largest_circuits[1] * largest_circuits[2]))

