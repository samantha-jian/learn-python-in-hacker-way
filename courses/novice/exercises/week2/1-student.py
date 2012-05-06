#!/usr/bin/env python
answer = None
data = [ [1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15] ]

data.insert(2, 'A')
#I created a list attribute so that "AttributeError: 'NoneType' object has no attribute 'extend'" will not happen. type(answer) is NoneType. 
tmp = [] 
for i in range(len(data)):
	tmp.extend(data[i])

answer = tmp

assert answer == [1,2,3,4,5,6,7,8, 9,10, 'A', 11,12,13,14,15], answer
