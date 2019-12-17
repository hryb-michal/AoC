#!/usr/bin/python

import os

input_file = open('input.txt', 'r')

intcode = input_file.read()
base_arr = [int(s) for s in intcode.split(',')]

def step(pos, arr):
	if(arr[pos] == 1):
		arr[arr[pos+3]] = arr[arr[pos+1]] + arr[arr[pos+2]]
	elif(arr[pos] == 2):
		arr[arr[pos+3]] = arr[arr[pos+1]] * arr[arr[pos+2]]
	elif(arr[pos] == 99):
		return False
	else:
		return False
	return True

def run(arr, noun, verb):
	arr[1] = noun
	arr[2] = verb
	pos = 0
	while(step(pos, arr)):
		pos = pos+4	

def find(arr, base_arr):
	for i in range(0, 100):
		for j in range (0, 100):
			run(arr, i, j)
			if(i == 12 and j == 2):
				print("1st solution:", arr[0])
			if (arr[0] == 19690720):
				print("2nd solution:", arr[1], arr[2])
			arr = base_arr.copy()

arr = base_arr.copy()
find(arr, base_arr)



