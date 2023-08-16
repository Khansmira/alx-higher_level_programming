#!/usr/bin/python3



import sys
import signal


total_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_statistics():
    """
    Print the current statistics, including total file size and status code counts.
    """
    global total_size, status_code_count
    print("File size:", total_size)
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def signal_handler(sig, frame):
    """
    Handle the keyboard interrupt (CTRL+C) signal by printing statistics and exiting.
    """
    print_statistics()
    sys.exit(0)

try:
    line_count = 0
    for line in sys.stdin:
        try:
            _, _, _, _, _, status_code, file_size = line.split()[3:]
            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics()
        except (ValueError, IndexError):
            pass
except KeyboardInterrupt:
    pass

print_statistics()

