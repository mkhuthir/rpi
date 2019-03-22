#! /usr/bin/python3

import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 30)

pixels[0]=(0,0,0)


