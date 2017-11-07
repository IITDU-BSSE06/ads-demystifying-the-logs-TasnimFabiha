#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
thisCounter = 0
maxPathCounter = -9999999
# Loop around the data
# It will be in the format key\tval
# Where key is the file path, val is the file path hit amount



for line in sys.stdin:
	data_mapped = line.strip()
	thisKey = data_mapped
    
	if oldKey and oldKey != thisKey:
		if maxPathCounter < thisCounter:
			maxKey = oldKey
		
    thisCounter = 0
	
  oldKey = thisKey
	thisCounter = thisCounter+1
    

print maxPathCounter

