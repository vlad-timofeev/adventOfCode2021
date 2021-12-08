""" day 7 part 2"""

coordinates = []

with open('input.txt', 'r', encoding='UTF-8') as input_file:
    coordinates = list(map(int, input_file.readline().split(',')))

min_coordinate, max_coordinate = min(coordinates), max(coordinates)

number_of_crabs_by_coordinate = [0] * (max_coordinate + 1)

for coordinate in coordinates:
    number_of_crabs_by_coordinate[coordinate] += 1


diff_suffix_sums = [0] * (max_coordinate + 1)
crabs_to_the_right = 0
prev_sum = 0
for index in range(max_coordinate, -1, -1):
    diff_suffix_sums[index] = prev_sum + crabs_to_the_right
    current_crabs = number_of_crabs_by_coordinate[index]
    crabs_to_the_right += current_crabs
    prev_sum = diff_suffix_sums[index]

diff_prefix_sums = [0] * (max_coordinate + 1)
crabs_to_the_left = 0
prev_sum = 0
for index in range(0, max_coordinate + 1):
    diff_prefix_sums[index] = prev_sum + crabs_to_the_left
    current_crabs = number_of_crabs_by_coordinate[index]
    crabs_to_the_left += current_crabs
    prev_sum = diff_prefix_sums[index]


def fuel_by_coord_diff(diff):
    return (diff * (1 + diff) // 2)


required_fuel = sum(fuel_by_coord_diff(n) for n in coordinates)
best_required_fuel = required_fuel

for coordinate in range(min_coordinate, max_coordinate):
    required_fuel = required_fuel + \
        diff_prefix_sums[coordinate + 1] - diff_suffix_sums[coordinate]
    best_required_fuel = min(best_required_fuel, required_fuel)

print(best_required_fuel)
