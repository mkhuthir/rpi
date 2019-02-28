#!/usr/bin/python

from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

    	x = abs(x)
    	y = abs(y)
    	z = abs(z)

    	if x > 2 or y > 2 or z > 2:
        	sense.show_letter("!", red)
    	else:
        	sense.clear()
