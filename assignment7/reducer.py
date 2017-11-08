#!/usr/bin/python


import sys

count1 = 0
count2 = 0
#count3 = 0
a = "GET"
b = "POST"


for line in sys.stdin:
	data_mapped = line.strip()
    	if not data_mapped :
        	continue
	if data_mapped[1:] == a:
		count1 = count1+1
	if data_mapped[1:] == b:
		count2 = count2+1
print a, "\t", count1
print b, "\t", count2
