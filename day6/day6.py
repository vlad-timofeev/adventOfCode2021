""" day 6 """
REPLICATION_PERIOD_DAYS = 7
FIRST_CYCLE_EXTRA_DAYS = 2
# part1 - 80, part2 - 256
DAYS_OF_REPLICATION = 256

initial_fish_timers = []

with open('input.txt', 'r', encoding='UTF-8') as input_file:
    initial_fish_timers = list(map(int, input_file.readline().split(',')))

fishes_grouped_by_timer = [0] * \
    (REPLICATION_PERIOD_DAYS + FIRST_CYCLE_EXTRA_DAYS)

for timer in range(REPLICATION_PERIOD_DAYS):
    fishes_grouped_by_timer[timer] = initial_fish_timers.count(timer)


for _ in range(DAYS_OF_REPLICATION):
    temp_array = [0] * \
        (REPLICATION_PERIOD_DAYS + FIRST_CYCLE_EXTRA_DAYS)
    temp_array[REPLICATION_PERIOD_DAYS - 1] = fishes_grouped_by_timer[0]
    temp_array[REPLICATION_PERIOD_DAYS +
               FIRST_CYCLE_EXTRA_DAYS - 1] = fishes_grouped_by_timer[0]
    for timer in range(REPLICATION_PERIOD_DAYS + FIRST_CYCLE_EXTRA_DAYS - 1):
        temp_array[timer] += fishes_grouped_by_timer[timer + 1]

    fishes_grouped_by_timer = temp_array

print(sum(fishes_grouped_by_timer))
