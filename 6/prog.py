#!/usr/env/python


import os

input_file = open('input.txt', 'r')

orbits = [str(line) for line in input_file]

class Planet:

 	def __init__(self, value):
 		self.value = value
 		self.children = set([])

 	def insert_orbiting(self, Planet):
 		self.children.add(Planet)


def count_orbiting_planets(Root_planet, counter = 0, level = 0):
	counter += level
	for planet in Root_planet.children:
		counter = count_orbiting_planets(planet, counter, level+1)
	return counter

class Planet_manager:
	def __init__(self, Root_planet):
		self.route = []
		self.Root_planet = Root_planet

	def route_to_planet_exists(self, destination, planet = None):
		if planet is None:
			planet = self.Root_planet

		if(planet.value == destination):
			return True
		elif(len(planet.children) == 0):
			return False
		else:
			for child in planet.children:
				if(self.route_to_planet_exists(destination, child)):
					self.route.append(planet.value)
					return True
			return False

	def find_route_to(self, destination):
		if(self.route_to_planet_exists(destination)):
			print("Route to", destination, "found!")
		else:
			print("no such route!")


dependencies = {}
for orbit in orbits:
	planets = orbit.split(')')
	x = planets[0].rstrip()
	y = planets[1].rstrip()

	if(x not in dependencies):
		dependencies[x] = []
	dependencies[x].append(y)

def create_map (papa_planet, orbiting_planets):
	for orbiting_planet in orbiting_planets:
		orbiting_planet = Planet(orbiting_planet)
		papa_planet.insert_orbiting(orbiting_planet)
		if orbiting_planet.value in dependencies:
			create_map(orbiting_planet, dependencies[orbiting_planet.value])

papa_planet = Planet("COM")
orbiting_planets = dependencies[papa_planet.value]	

create_map(papa_planet, orbiting_planets)

total_orbits = count_orbiting_planets(papa_planet)

print("Total orbits:", total_orbits)


Route1 = Planet_manager(papa_planet)
Route2 = Planet_manager(papa_planet)

Route1.find_route_to("YOU")
Route2.find_route_to("SAN")

unique_route = set(Route1.route) ^ set(Route2.route)

print(len(unique_route))
