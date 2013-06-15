#!/usr/bin/python3
# Head ends here
import math

def findPrincess(n,grid):
	x = 0
	y = 0
	for line in grid:
		try:
			x = line.index('p')
			break
		except:
			y = y+1;
	return (x,y)
	
def nextMove(n,x,y,grid):
	princess = findPrincess(n,grid);
	if (princess[0]<x):
		# go left
		return "LEFT"
	elif (princess[0]>x):
		# go right
		return "RIGHT"

	if (princess[1]<y):
		# go up
		return "UP"
	else:
		# go down
		return "DOWN"
    
# Tail starts here
n = int(input())
y,x = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,x,y,grid))
