#!/usr/bin/python3
import sys


def print_stats(total_size, status_counts):
    """
    Print statistics including total file size and status code counts.

    Args:
        total_size (int): Total size of files.
        status_counts (dict): Dictionary containing status code counts.
    """
    print("File size:", total_size)
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")


def parse_line(line):
    """
    Parse a log line and extract IP, status code, and file size.

    Args:
        line (str): Log line to parse.

    Returns:
        tuple or None: Tuple containing IP address, status code,
        and file size if parsing is successful, otherwise None.
    """
    parts = line.split()
    if len(parts) < 9:
        return None
    ip, _, _, _, status, size = parts[:6] + parts[-2:]
    if status.isdigit():
        return ip, int(status), int(size)
    return None


def main():
    """
    Main function to read log data from stdin,
    compute statistics, and print results.
    """
    total_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        for i, line in enumerate(sys.stdin, start=1):
            parsed = parse_line(line.strip())
            if parsed:
                ip, status, size = parsed
                total_size += size
                status_counts[status] += 1
            if i % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
