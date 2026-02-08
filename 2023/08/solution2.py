file = open("input.txt", "r")
lines = file.read().splitlines()

directions = lines[0]

# parse each line as AAA = (BBB, CCC) into a dictionary of the form {AAA: (BBB, CCC)}
mapping = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}
nodes = [node for node in mapping.keys() if node[2] == 'A']

def length_to_znode(starting_node):
    instructions = 0
    node = starting_node

    while node[2] != 'Z':
        node = mapping[node][0] if directions[instructions % len(directions)] == "L" else mapping[node][1]
        instructions += 1

    return instructions

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


lengths = [length_to_znode(node) for node in nodes]

lcm_length = 1
for length in lengths:
    lcm_length = lcm(lcm_length, length)

print(lcm_length)