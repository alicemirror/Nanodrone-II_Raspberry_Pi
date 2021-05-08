#!/bin/bash
# Pi Camera Control

echo "PiCamera capture with raspistill"

# Camera preview
raspistill --preview '250,250,800,600' --rotation 180 -o ~/Pictures/test01.jpg


