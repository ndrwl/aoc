import math

file = open("input.txt", "r")
lines = file.read().splitlines()

time = int(''.join([x for x in lines[0].split(' ')[1:] if x.strip() != '']))
distances = int(''.join([x for x in lines[1].split(' ')[1:] if x.strip() != '']))

# We are solving for the equation 0 > x^2 - tx + d, where t is time and d is distance. We can use the quadratic formula
# to find the roots of this equation.

discriminant = time**2 - 4 * distances
solution1 = (time + discriminant**0.5) / 2
solution2 = (time - discriminant**0.5) / 2

print("Minimum speed: %d" % math.floor(min(solution1, solution2) + 1))
print("Maximum speed: %d" % math.ceil(max(solution1, solution2) - 1))

range = math.ceil(max(solution1, solution2) - 1) - math.floor(min(solution1, solution2) + 1) + 1
print("Range of speeds: %d" % range)