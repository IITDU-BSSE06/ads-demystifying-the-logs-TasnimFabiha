#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
thisCounter = 0
maxPathCounter = -9999999
# Loop around the data
# It will be in the format key\tval
# Where key is the file path, val is the unique file count

uniquefile = 1

for line in sys.stdin:
	data_mapped = line.strip()
	thisKey = data_mapped
    
	if oldKey and oldKey != thisKey:
		uniquefile = uniquefile + 1
		
	
	oldKey = thisKey
	
    

print uniquefile
