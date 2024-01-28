
#To run use
#python cat_shelter.py shelter_2023-08-25.log
#python cat_shelter.py shelter_2023-08-26.log
#python cat_shelter.py shelter_2023-08-27.log

import sys

def process_log_file(filename):
    # Analyzes a log file from a cat shelter and prints statistics
    # about cat visits, including total visit time, average visit length,
    # longest visit, and shortest visit.
    # Analyzes a log file from a cat shelter and prints statistics 
    # about cat visits, including total visit time, average visit length, 
    # longest visit, and shortest visit.
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{filename}"!')
        return

    cat_visits = 0
    other_cats = 0
    total_time = 0
    visit_lengths = []

    for line in lines:
        if line.strip() == 'END':
            break
        parts = line.split(',')
        cat_type, start, end = parts[0], int(parts[1]), int(parts[2])
        duration = end - start

        if cat_type == 'OURS':
            cat_visits += 1
            total_time += duration
            visit_lengths.append(duration)
        elif cat_type == 'THEIRS':
            other_cats += 1

    if cat_visits > 0:
        avg_visit_length = total_time // cat_visits
        longest_visit = max(visit_lengths)
        shortest_visit = min(visit_lengths)
    else:
        avg_visit_length = longest_visit = shortest_visit = 0

    hours, minutes = divmod(total_time, 60)

    print("\nLog File Analysis")
    print("==================\n")
    print(f"Cat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}\n")
    print(f"Total Time in House: {hours} Hours, {minutes} Minutes\n")
    print(f"Average Visit Length: {avg_visit_length} Minutes")
    print(f"Longest Visit:        {longest_visit} Minutes")
    print(f"Shortest Visit:       {shortest_visit} Minutes\n")

def main():
    if len(sys.argv) < 2:
        print("Missing command line argument!")
        return

    filename = sys.argv[1]
    process_log_file(filename)

if __name__ == "__main__":
    main()
