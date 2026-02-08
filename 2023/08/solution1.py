file = open("input.txt", "r")
lines = file.read().splitlines()

directions = lines[0]

# parse each line as AAA = (BBB, CCC) into a dictionary of the form {AAA: (BBB, CCC)}
mapping = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

instructions = 0
node = "AAA"

while node != "ZZZ":
    node = mapping[node][0] if directions[instructions % len(directions)] == "L" else mapping[node][1]
    instructions += 1

print("Instructions: %d" % instructions)