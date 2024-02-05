"""
Module to compute statistics from a file.
"""

import sys
import time
import statistics

def compute_statistics(file_path):
    """
    Compute decriptive statistics from a file.
    
    - param FILE_PATH: Path to the file containing data.
    """

    data = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        data.append(float(line))
                    except ValueError:
                        print(f"Warning: Skipping invalid entry: {line}")

        if not data:
            print("No valid data.")
            return
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    mean_value = sum(data) / len(data)
    median_value = statistics.median(data)
    mode_value = statistics.mode(data) if len(data) > 0 else None
    stdev_value = statistics.stdev(data) if len(data) > 1 else None
    variance_value = statistics.variance(data) if len(data) > 1 else None

    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Mode: {mode_value}")
    print(f"Standard Deviation: {stdev_value}")
    print(f"Variance: {variance_value}")

    with open('StatisticsResults.txt', 'a', encoding='utf-8') as results_file:
        results_file.write(f"Mean: {mean_value}\n")
        results_file.write(f"Median: {median_value}\n")
        results_file.write(f"Mode: {mode_value}\n")
        results_file.write(f"Standard Deviation: {stdev_value}\n")
        results_file.write(f"Variance: {variance_value}\n")

if __name__ == "__main__":
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Path to data file not in call.")
    else:
        FILE_PATH = sys.argv[1]
        compute_statistics(FILE_PATH)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Execution Time: {elapsed_time}s")

    with open('StatisticsResults.txt', 'a', encoding='utf-8') as results_file_append:
        results_file_append.write(f"Execution Time for {FILE_PATH}: {elapsed_time}s\n")
        results_file_append.write("\n_____________________________\n")
