"""Count and print word frequency in a text file."""

import sys
import time

def count_and_print_word_frequency(file_path):
    """
    Count and print the word frequency in the specified text file.

    Parameters:
    - file_path: Path to the text file.
    """
    start_time = time.time()

    word_frequency = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    # Update word frequency
                    word_frequency[word] = word_frequency.get(word, 0) + 1

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Print results on the screen
    print("Word Frequency:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

    # Save results to file
    with open('WordCountResults.txt', 'a', encoding='utf-8') as results_file:
        results_file.write("Word Frequency:\n")
        for word, frequency in word_frequency.items():
            results_file.write(f"{word}: {frequency}\n")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print and save elapsed time
    print(f"\nExecution Time: {elapsed_time}s")
    with open('WordCountResults.txt', 'a', encoding='utf-8') as results_file:
        results_file.write(f"\nExecution Time: {elapsed_time}s\n")
        results_file.write("\n\n_____________________________\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Path to data file not in call.")
    else:
        FILE_PATH = sys.argv[1]
        count_and_print_word_frequency(FILE_PATH)
