#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
thisCounter = 0
maxPathCounter = -9999999
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data_mapped = line.strip()
	thisKey = data_mapped
    
	if oldKey and oldKey != thisKey:
		if maxPathCounter < thisCounter:
			maxPathCounter = thisCounter
			maxKey = oldKey
		thisCounter = 0
	oldKey = thisKey
	thisCounter = thisCounter+1
    
#maxPath = max(maxPathCounter, thisCounter)
print maxPathCounter
print maxKey
