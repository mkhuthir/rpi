#!/bin/bash

DATE=$(date +"%Y_%m_%d-%H_%M_%S")

# record a 2 sec video
raspivid -t 2000 -o $DATE.h264
