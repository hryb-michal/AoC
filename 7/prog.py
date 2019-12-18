#!/usr/bin/python

import itertools
input_file = open('input.txt', 'r')
intcode = input_file.read()
base_arr = [int(s) for s in intcode.split(',')]


'''
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
'''

class IntcodeParser:
	index = 0 #ind of inputs provided to program so far
	output_value = 0
	opcode = 0
	pos = 0 	#current position in array
	step_val = 0	#current next step value
	step_values = { 1: 4,   #step value depending on opcode value
				    2: 4,
				    3: 2,
				    4: 2,
				    5: 3,
				    6: 3,
				    7: 4,
				    8: 4 }

	def __init__(self, arr, phase, input_value):
		self.arr = arr
		self.input_value = [phase, input_value]

	def value_by_mode(self, mode, position):
		if(mode == 1): #immediate mode
			return self.arr[position]
		if(mode == 0): #position mode
			return self.arr[self.arr[position]]

	def step(self, pos):
		#print("\n")
		modes = [0, 0, 0] #A, B, C
		instruction = str(self.arr[pos])
		if(len(instruction) >= 2):
			self.opcode = int(instruction[-2:])
			i = 0
			raw_modes = instruction[:-2]
			for mode in raw_modes[::-1]:
				modes[i] = int(mode)  #modes: C, B, A
				i+=1
			modes = modes[::-1] #modes: A, B, C
		else:
			self.opcode = int(instruction)

		#print("opcode:", self.opcode, "modes:", modes)

		if(self.opcode == 1):
			res = self.value_by_mode(modes[2], pos+1) + self.value_by_mode(modes[1], pos+2)
			self.arr[self.arr[pos+3]] = res

		elif(self.opcode == 2): #multiply two next values
			#print(self.arr[pos:pos+4])
			self.arr[self.arr[pos+3]] = self.value_by_mode(modes[2], pos+1) * self.value_by_mode(modes[1], pos+2)
		
		elif(self.opcode == 3): #read input and store it to next value
			#print("current input:", self.input_value[self.index])
			self.arr[self.arr[pos+1]] = self.input_value[self.index]
			self.index += 1

		elif(self.opcode == 4): #store output to next value
			self.output_value = self.value_by_mode(modes[2], pos+1)
			#print(self.output_value)

		elif(self.opcode == 5):
			#print("jump-if-true:", self.arr[pos:pos+3])
			if(self.value_by_mode(modes[2], pos+1) != 0):
				self.step_val = self.value_by_mode(modes[1], pos+2) - self.pos
				return True 

		elif(self.opcode == 6):
			if(self.value_by_mode(modes[2], pos+1) == 0):
				self.step_val = self.value_by_mode(modes[1], pos+2) - self.pos
				return True 

		elif(self.opcode == 7):
			if(self.value_by_mode(modes[2], pos+1) < self.value_by_mode(modes[1], pos+2)):
				self.arr[self.arr[pos+3]] = 1
			else:
				self.arr[self.arr[pos+3]] = 0

		elif(self.opcode == 8):
			if(self.value_by_mode(modes[2], pos+1) == self.value_by_mode(modes[1], pos+2)):
				self.arr[self.arr[pos+3]] = 1
			else:
				self.arr[self.arr[pos+3]] = 0

		elif(self.arr[pos] == 99):
			#print("end!")
			return False
		else:
			#print("error!")
			return False
		self.step_val = self.step_values[self.opcode]
		return True

	def run(self):
		while(self.step(self.pos)):
			self.pos += self.step_val

base_phases = [0, 1, 2, 3, 4]
permutations = itertools.permutations(base_phases)
highest_output = 0

for phases in list(permutations):
	next_param = 0
	for phase in phases:
		Amplifier = IntcodeParser(base_arr, phase, next_param) #solution for part 2
		Amplifier.run()
		next_param = Amplifier.output_value
	if(next_param > highest_output):
		highest_output = next_param
print("Part 1:", highest_output)


base_phases = [5, 6, 7, 8, 9]
permutations = itertools.permutations(base_phases)
highest_output = 0

for phases in list(permutations):
	next_param = 0

	for phase in phases:
		Amplifier = IntcodeParser(base_arr, phase, next_param) #solution for part 2
		Amplifier.run()
		next_param = Amplifier.output_value
	if(next_param > highest_output):
		highest_output = next_param
print("Part 1:", highest_output)