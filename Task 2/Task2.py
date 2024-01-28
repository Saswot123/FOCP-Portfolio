import sys
import os

def analyze_log_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        sys.exit(1)

    cat_visits = 0
    intruder_dousing = 0
    total_time_in_house = 0
    cat_visit_lengths = []

    for line in lines:
        if line.strip() == 'END':
            break

        data = line.strip().split(',')
        cat_name, entry_time, exit_time = data[0], int(data[1]), int(data[2])

        if cat_name == 'OURS':
            cat_visits += 1
            total_time_in_house += (exit_time - entry_time)
            cat_visit_lengths.append(exit_time - entry_time)
        elif cat_name == 'THEIRS':
            intruder_dousing += 1

    if cat_visits == 0:
        average_visit_length = longest_visit = shortest_visit = 0
    else:
        average_visit_length = sum(cat_visit_lengths) / cat_visits
        longest_visit = max(cat_visit_lengths)
        shortest_visit = min(cat_visit_lengths)

    return cat_visits, intruder_dousing, total_time_in_house, average_visit_length, longest_visit, shortest_visit


def format_time(minutes):
    hours, mins = divmod(minutes, 60)
    return f'{int(hours)} Hours, {int(mins)} Minutes'


def main():
    if len(sys.argv) != 2:
        print('Missing command line argument!')
        sys.exit(1)

    file_path = sys.argv[1]

    cat_visits, intruder_dousing, total_time_in_house, average_visit_length, longest_visit, shortest_visit = analyze_log_file(file_path)

    print("\nLog File Analysis\n==================\n")
    print(f'Cat Visits: {cat_visits}')
    print(f'Other Cats: {intruder_dousing}\n')
    print(f'Total Time in House: {format_time(total_time_in_house)}\n')
    print(f'Average Visit Length: {format_time(average_visit_length)}')
    print(f'Longest Visit:        {format_time(longest_visit)}')
    print(f'Shortest Visit:       {format_time(shortest_visit)}')


if __name__ == "__main__":
    main()