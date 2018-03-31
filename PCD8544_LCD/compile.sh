#!/bin/bash

gcc main.c lib/PCD8544.c -o main  -L/usr/local/lib -lwiringPi
