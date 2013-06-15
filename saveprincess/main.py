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

def displayPathtoPrincess(n,grid):
	#print(n, grid)
	princess = findPrincess(n,grid);
	#print(princess)
	
	if (princess[0]==0):
		# go left
		for i in range(0,math.trunc(n/2)):
			print("LEFT")
	else:
		# go right
		for i in range(0,math.trunc(n/2)):
			print("RIGHT")

	if (princess[1]==0):
		# go up
		for i in range(0,math.trunc(n/2)):
			print("UP")
	else:
		# go down
		for i in range(0,math.trunc(n/2)):
			print("DOWN")
		
#print all the moves here
# Tail starts here
m = int(input())
grid = [] 
for i in range(0, m):
	grid.append(input().strip())

displayPathtoPrincess(m,grid)

