#!/usr/bin/env python

import random

nums = []
size = 50

for i in xrange(size):
    r = random.randint(1, 100)
    nums.append(r)

nums.sort()

# print nums

key = random.randint(1, 100)

print "Your key is %d" %key

found = False

print "Doing linear search"

for i in xrange(len(nums)):
    v = nums[i]
    if key == v:
        found = True
        print "%d is found at position %d." % (key, i)

if not found:
    print "%d is not found." %key
    
print "Doing binary search"

lo = 0
hi = size - 1

found = False

while hi >= lo:
    med = (hi + lo) / 2
    med_number = nums[med]
    lo_number = nums[lo]
    hi_number = nums[hi]
    if med_number > key:
        hi = med - 1
    elif med_number < key:
        lo = med + 1
    else:
        found = True
        print "%d is found at position %d." %(key, med)
        up = med - 1
        down = med + 1
        while up >= 0 and nums[up] == key:
            print "%d is found at position %d." %(key, up)
            up -= 1
        while down < size and nums[down] == key:
            print "%d is found at position %d." %(key, down)
            down += 1
        exit()
        
if not found:
    print "%d is not found" %key


    
    




















    