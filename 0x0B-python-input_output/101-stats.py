#!/usr/bin/python3
"""
This script reads from standard input and calculates metrics.
"""

def display_metrics(total_file_size, status_code_counts):
    """Print accumulated metrics."""
    print("Total file size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        print("{}: {}".format(code, status_code_counts[code]))

if __name__ == "__main__":
    import sys

    total_file_size = 0
    status_code_counts = {}
    valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_counter = 0

    try:
        for line in sys.stdin:
            if line_counter == 10:
                display_metrics(total_file_size, status_code_counts)
                line_counter = 1
            else:
                line_counter += 1

            parts = line.split()

            try:
                total_file_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_status_codes:
                    if status_code_counts.get(parts[-2], -1) == -1:
                        status_code_counts[parts[-2]] = 1
                    else:
                        status_code_counts[parts[-2]] += 1
            except IndexError:
                pass

        display_metrics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        display_metrics(total_file_size, status_code_counts)
        raise
