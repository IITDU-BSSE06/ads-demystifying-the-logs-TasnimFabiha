#!/usr/bin/python


import sys

count1 = 0
count2 = 0
count3 = 0


for line in sys.stdin:
	data_mapped = line.strip()
    	if not data_mapped :
        	continue
	year = data_mapped.split("/")
	if year[2][:4] == "2009": 
		count1 = count1+1
	if year[2][:4] == "2010": 
		count2 = count2+1
	if year[2][:4] == "2011": 
		count3 = count3+1
		

	
print "2009", "\t", count1
print "2010", "\t", count2
print "2011", "\t", count3
