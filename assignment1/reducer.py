#!/usr/bin/python

import sys


count = 0
for line in sys.stdin:
    data = line.strip()
    if not data:
        # Something has gone wrong. Skip this line.
        continue
    if data == "10.99.99.186":
        count = count+1

print count


