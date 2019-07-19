#!/bin/bash

DATE=$(date +"%Y_%m_%d-%H_%M_%S")

raspistill -vf -hf -o $DATE.jpg

