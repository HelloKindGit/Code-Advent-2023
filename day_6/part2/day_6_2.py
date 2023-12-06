def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    time_distance = (int(lines[0].split(':')[1].replace(" ", "").strip()),
                     int(lines[1].split(':')[1].replace(" ", "").strip()))
        
    return time_distance

def ways_to_beat_record(time_distance):
    time, distance = time_distance
    ways = 0

    for hold_time in range(time + 1):
        boat_speed = hold_time #Speed increases by 1 for each millisecond held
        travel_time = time - hold_time
        total_distance = boat_speed * travel_time

        if total_distance > distance:
            ways += 1

    return ways

def calculate_possibilities(file_path):
    time_distance = read_input(file_path)

    ways = ways_to_beat_record(time_distance)

    return ways

file_path = "day_6/part2/input.txt" #"day_6/part2/test.txt"
results = calculate_possibilities(file_path)
print(results)