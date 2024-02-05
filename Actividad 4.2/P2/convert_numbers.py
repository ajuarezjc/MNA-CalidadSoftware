"""
This script reads numbers from a file,
converts them to binary and hexadecimal,
and prints the results.
"""

import sys
import time

def convert_and_print_results(input_data):
    """
    Convert numbers to binary and hexadecimal and print the results.

    Parameters:
    - data: List of integers to be converted.

    Returns:
    - tuple: Lists of binary values and hexadecimal values.
    """
    bin_values = []
    hex_values = []

    for input_number in input_data:
        # Convert number to binary
        bin_values.append(bin(input_number)[2:])
        # Convert number to hexadecimal
        hex_values.append(hex(input_number)[2:].upper())

    return bin_values, hex_values

if __name__ == "__main__":
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Path to data file not in call.")
    else:
        FILE_PATH = sys.argv[1]

        data = []

        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        try:
                            data.append(int(line))
                        except ValueError:
                            print(f"Warning: Skipping invalid entry: {line}")

            if not data:
                print("No valid data to convert.")
            else:
                # Convert and print results
                binary_values, hexadecimal_values = convert_and_print_results(data)

                # Save results to file
                with open('ConversionResults.txt', 'a', encoding='utf-8') as results_file:
                    for i, number in enumerate(data):
                        result = f"N:{number}, B:{binary_values[i]}, Hex:{hexadecimal_values[i]}\n"
                        results_file.write(result)

        except FileNotFoundError:
            print(f"Error: File '{FILE_PATH}' not found.")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Execution Time: {elapsed_time}s")

    with open('ConversionResults.txt', 'a', encoding='utf-8') as results_file:
        results_file.write(f"\nExecution Time for {FILE_PATH}: {elapsed_time}s\n")
        results_file.write("\n\n_____________________________\n\n")
