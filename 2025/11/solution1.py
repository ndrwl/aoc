import queue

file = open("input.txt", "r")
lines = file.read().splitlines()

def count_paths(graph, start, target, must_visit=None):
    if must_visit is None:
        must_visit = []

    reverse_graph = {}
    explore_queue = queue.Queue()
    explore_queue.put((start, 0))

    # first pass - build reverse graph
    while not explore_queue.empty():
        node, visit_mask = explore_queue.get()
        new_visit_mask = visit_mask
        if node in must_visit:
            new_visit_mask |= (1 << must_visit.index(node))

        for neighbor_node in graph.get(node, []):
            neighbor = (neighbor_node, new_visit_mask)

            if neighbor not in reverse_graph:
                reverse_graph[neighbor] = []
                explore_queue.put(neighbor)
            reverse_graph[neighbor].append((node, visit_mask))

    # second pass - evaluate each node
    path_counts = {}
    pending_explorations = {(start, 0)}
    explore_queue.put((start, 0))
    goal = (target, (1 << len(must_visit)) - 1)

    while not explore_queue.empty():
        element = explore_queue.get()
        node, visit_mask = element

        if any(previous_node not in path_counts for previous_node in reverse_graph.get(element, [])):
            # requeue this node until all parents are evaluated
            explore_queue.put(element)
            continue

        pending_explorations.remove(element)

        # update path_count
        path_counts[element] = sum(path_counts[previous_node] for previous_node in reverse_graph.get(element, [])) if node != start else 1

        if element == goal:
            return path_counts[element]

        # enqueue neighbors
        new_visit_mask = visit_mask
        if node in must_visit:
            new_visit_mask |= (1 << must_visit.index(node))

        for neighbor_node in graph.get(node, []):
            neighbor = (neighbor_node, new_visit_mask)
            if neighbor not in path_counts and neighbor not in pending_explorations:
                explore_queue.put(neighbor)
                pending_explorations.add(neighbor)

    return 0

graph = {}

for line in lines:
    input = line[:line.index(':')]
    outputs = line[line.index(':')+2:].split(' ')
    graph[input] = outputs

print("Total paths from you to out: %d" % count_paths(graph, 'you', 'out'))
print("Total paths from svr to out (passing dac and fft): %d" % count_paths(graph, 'svr', 'out', must_visit=['dac', 'fft']))
