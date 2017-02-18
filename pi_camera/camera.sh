#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H:%M:%S")

raspistill -vf -hf -o /home/pi/camera/$DATE.jpg

