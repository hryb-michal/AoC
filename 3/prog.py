#!/usr/env/python


import os

input_file = open('input.txt', 'r')

ways = [str(line) for line in input_file]
wires = [ways[0].split(','), ways[1].split(',')]

pos = (0,0)
visited = []
visited2 = []
intersections = []
distances = {}
distances2 = {}

num = 0
for wire in wires:
	x = 0
	y = 0
	d = 0
	for move in wire:
		print(move)
		direction = move[0]
		if (direction == 'L'):
			new_x = x - int(move[1:])
			for i in range (x, new_x, -1):
				d+=1
				if not num:
					visited.append((i,y))
					distances[(i,y)] = d
				else:
					visited2.append((i,y))
					distances2[(i,y)] = d
			x = new_x

		elif (direction == 'R'):
			new_x = x + int(move[1:])
			for i in range (x+1, new_x+1):
				d+=1
				if not num:
					visited.append((i,y))
					distances[(i,y)] = d
				else:
					visited2.append((i,y))
					distances2[(i,y)] = d
			x = new_x

		elif (direction == 'U'):
			new_y = y + int(move[1:])
			for i in range (y+1, new_y+1):
				d=d+1
				if not num:
					visited.append((x,i))
					distances[(x,i)] = d
				else:
					visited2.append((x,i))
					distances2[(x,i)] = d
			y = new_y

		elif (direction == 'D'):
			new_y = y - int(move[1:])
			for i in range (y, new_y, -1):
				d=d+1
				if not num:
					visited.append((x,i))
					distances[(x,i)] = d
				else:
					visited2.append((x,i))
					distances2[(x,i)] = d
			y = new_y
	num += 1


intersections = list(set(visited).intersection(visited2))
print(intersections)

sums = []
distances_summed = []
for intersection in intersections:
	sums.append(abs(intersection[0]) + abs(intersection[1]))
	distances_summed.append(distances[intersection] + distances2[intersection])

distances_summed.sort()
sums.sort()
print(sums[0])
print(distances_summed[0])