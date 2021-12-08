""" day 7 """

coordinates = []

with open('input.txt', 'r', encoding='UTF-8') as input_file:
    coordinates = list(map(int, input_file.readline().split(',')))

min_coordinate, max_coordinate = min(coordinates), max(coordinates)


number_of_crabs_by_coordinate = [0] * (max_coordinate + 1)

for coordinate in coordinates:
    number_of_crabs_by_coordinate[coordinate] += 1

# "required_fuel" is fuel required to get all crabs to 0 coordinate
best_required_fuel = required_fuel = sum(coordinates)

crabs_to_the_left = 0
crabs_to_the_right = len(coordinates)

for coordinate in range(min_coordinate, max_coordinate + 1):
    current_crabs = number_of_crabs_by_coordinate[coordinate]
    crabs_to_the_left += current_crabs
    crabs_to_the_right -= current_crabs
    required_fuel = required_fuel + crabs_to_the_left - crabs_to_the_right
    best_required_fuel = min(best_required_fuel, required_fuel)

print(best_required_fuel)
