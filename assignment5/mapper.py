#!/usr/bin/python

# Format of each line is:
#10.247.111.104 - - [07/Sep/2010:05:14:50 -0700] "GET / HTTP/1.1" 200 4172
# We want 7th elements  separated by space
# We need to write them out to standard output

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    print data[6]


