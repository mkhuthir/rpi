#!/usr/bin/python

from sense_hat import SenseHat

sense = SenseHat()

while True:
	print(sense.get_compass())
