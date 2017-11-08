#!/usr/bin/python


import sys
from urllib.parse import urlparse



for line in sys.stdin:
	data_mapped = line.strip()
    	if not data_mapped :
        	continue

	thisKey = data_mapped
    
    if oldKey and oldKey != thisKey:
        print oldKey
        oldKey = thisKey;
        total = 0

    oldKey = thisKey
    total = total+1

if oldKey != None:
    print oldKey
