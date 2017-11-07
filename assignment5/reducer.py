#!/usr/bin/python

import sys

oldKey = None
uniquefile = 1
# Loop around the data
# It will be in the format key\tval
# Where key is the file path, val is the unique file count



for line in sys.stdin:
	data_mapped = line.strip()
	if not data_mapped :
        	# Something has gone wrong. Skip this line.
        	continue
	thisKey = data_mapped
    
	if oldKey and oldKey != thisKey:
		uniquefile = uniquefile + 1
		
	
	oldKey = thisKey
	
    

print uniquefile
