from collections import defaultdict, Counter
import sys
from pathlib import Path

def parse_log_line(line: str) -> dict:
    """
    Parse a single line from a log file into a structured dictionary.

    Args:
        line (str): A line from the log file. 
                    Expected format: "<DATE> <TIME> <LEVEL> <MESSAGE>"

    Returns:
        dict: A dictionary with the following keys:
            - "date" (str): Date of the log entry.
            - "time" (str): Time of the log entry.
            - "log_type" (str): Log level (e.g., INFO, ERROR, WARNING).
            - "log_text" (str): Remaining text of the log message.

    Raises:
        IndexError: If the log line is malformed or missing fields.
        ValueError: If the log line cannot be split correctly.
    """
    d = {}

    splitted_line = line.split()

    d["date"] = splitted_line[0]
    d["time"] = splitted_line[1]
    d["log_type"] = splitted_line[2]
    d["log_text"] = " ".join(splitted_line[3:])

    return d

def load_logs(file_path: str) -> list:
    """
    Load and parse all lines from a given log file.

    Args:
        file_path (str): Path to the log file to be read.

    Returns:
        list[dict]: A list of dictionaries, each representing a parsed log line.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be opened due to access restrictions.
        UnicodeDecodeError: If the file contains invalid UTF-8 symbols.
    """
    with open(file_path, "r", encoding="utf-8", errors='ignore') as file:
        lines = []
        for line in file:
            lines.append(parse_log_line(line))
    
    return lines
        

def filter_logs_by_level(logs: list, level: str):
    """
    Filter and display log entries that match the given log level.

    Args:
        logs (list[dict]): A list of parsed log dictionaries.
        level (str): The desired log level to display (e.g., "error", "info").
    """

    for log in logs:
        if log["log_type"].lower() == level:
            print(" ".join([log["date"], log["time"], "-", log["log_text"]]))

def count_logs_by_level(logs: list) -> dict:
    """
    Count the number of log entries for each log level.

    Args:
        logs (list[dict]): A list of parsed log dictionaries.

    Returns:
        dict: A dictionary mapping each log level to the number of occurrences.

    Example:
        {'INFO': 10, 'ERROR': 3, 'WARNING': 5}
    """
    logs_types = [log["log_type"] for log in logs]
    
    counted_types = Counter(logs_types)
    
    return counted_types

def display_log_counts(counts: dict):
    """
    Display a formatted summary table of log counts by level.

    Args:
        counts (dict): Dictionary where keys are log levels 
                       and values are counts of occurrences.

    Returns:
        None
    """

    print(f"{'Рівень логування':<18} | {'Кількість':>8}")
    print("-" * 18 + "|----------")

    total = 0
    for level in counts.keys():
        count = counts.get(level, 0)
        total += count
        print(f"{level:<18} | {count:>8}")

    print("-" * 18 + "|----------")
    print(f"{'TOTAL':<18} | {total:>8}")

def main():
    """
    Entry point for the log analysis script.

    The script loads and analyzes a log file, displaying counts of each log level,
    and optionally filtering logs by a specific level if provided as a second argument.

    Command-line usage:
        python task3.py <path_to_log_file> [log_level]

    Args:
        None (reads command-line arguments from sys.argv)

    Behavior:
        - Validates file path existence and type.
        - Parses the log file into structured data.
        - Prints the count of each log level.
        - If a log level is provided, prints all matching log lines.

    Raises:
        SystemExit: If arguments are missing, file not found, or invalid path.
    """
    if len(sys.argv) < 2:
        print(f"Error. Please add path to the txt file.")
        print(f"Example: python task3.py C:/Users/Admin/Pictures/logs.txt")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error '{file_path}' not exist.")
        sys.exit(1)

    if not file_path.is_file():
        print(f"Error: '{file_path}' is not file.")
        sys.exit(1)

    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    try:
        level = sys.argv[2]
    except:
        level = ""
    
    if level:
        filter_logs_by_level(logs, level)

    


if __name__ == "__main__":
    main()