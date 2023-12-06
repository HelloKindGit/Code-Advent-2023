def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    times = list(map(int, lines[0].split(':')[1].strip().split()))
    distances = list(map(int, lines[1].split(':')[1].strip().split()))
        
    return times, distances

def ways_to_beat_record(time, distance):
    ways = 0

    for hold_time in range(time + 1):
        boat_speed = hold_time #Speed increases by 1 for each millisecond held
        travel_time = time - hold_time
        total_distance = boat_speed * travel_time

        if total_distance > distance:
            ways += 1

    return ways

def calculate_possibilities(file_path):
    times, distances = read_input(file_path)
    
    total_ways = 1

    for i in range(len(times)):
        ways = ways_to_beat_record(times[i], distances[i])
        total_ways *= ways

    return total_ways

file_path = "day_6/part1/input.txt" #"day_6/part1/test.txt"
results = calculate_possibilities(file_path)
print(results)