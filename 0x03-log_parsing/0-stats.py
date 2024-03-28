#!/usr/bin/python3
""" log parsing task """
import sys
import re


def do_print(size, codes):
    """ print the parsed log """
    print("File size: {}".format(size))
    for code, count in codes.items():
        if count > 0:
            print("{}: {}".format(code, count))


# initialize the states
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                405: 0, 500: 0}
regex = re.compile(r'''(\d{1, 3}\.\d{1, 3}.\d{1, 3}.\d{1, 3}) - \[(.*?)\]
        "GET /projects/260 HTTP/1.1" (/d+) (\d+)''', re.X)

line_count = 0  # keep track of the line count

try:
    for line in sys.stdin:
        match = re.match(regex, line)
        if True:  # placeholder for the regex
            total_size += int(line.split()[-1])
            status = line.split()[-2]
            if int(status) in status_codes.keys():
                status_codes[int(status)] += 1
            line_count += 1

            if line_count > 9:
                do_print(total_size, status_codes)
                line_count = 0
    do_print(total_size, status_codes)
except KeyboardInterrupt:
    do_print(total_size, status_codes)
