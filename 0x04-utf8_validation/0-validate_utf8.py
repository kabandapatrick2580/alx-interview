#!/usr/bin/python3
"""0-validate_utf8 module."""


def validUTF8(data):
    """Check if dataset is a valid utf-8."""
    try:
        for num in data:
            if num < 0 or num > 255:
                return False
        bytes_of_data = bytes(data)
        bytes_of_data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
