#!/usr/bin/python

import os
import math

def required_fuel(mass):
	return (math.floor(mass/3)-2)

def total_required_fuel(module_mass):
	fuel = required_fuel(module_mass)
	current_mass = fuel

	while (required_fuel(fuel) > 0):
		fuel = required_fuel(fuel)
		current_mass += fuel

	return current_mass


input_file = open('input.txt', 'r')

summed = 0
total_sum = 0
for line in input_file:
	summed += required_fuel(int(line))
	total_sum += total_required_fuel(int(line))

print("fuel required: ", end=" ")
print(summed)
print("total fuel required:", end=" ")
print(total_sum)
