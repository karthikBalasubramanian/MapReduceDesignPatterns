#!/usr/bin/python

import sys

hitTotal = 0
oldKey = None
mostPop = None
maxHit = -1

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        if(max(maxHit,hitTotal)==hitTotal):
            maxHit = hitTotal
            mostPop = oldKey
        oldKey = thisKey
        hitTotal = 0


    oldKey = thisKey
    hitTotal += float(thisHit)

if oldKey != None:
    if(max(maxHit,hitTotal)==hitTotal):
            maxHit = hitTotal
            mostPop = oldKey
    print mostPop, "\t", maxHit

