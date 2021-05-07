#!/bin/bash
# Pi Camera Control

echo "PiCamera control with raspistill"

# Preview rotated
# raspistill --preview '250,250,800,600' --rotation 90
# raspistill --preview '250,250,800,600' --rotation 180
# raspistill --preview '250,250,800,600' --rotation 270

# raspistill --preview '250,250,800,600' --rotation 180 --hflip
# raspistill --preview '250,250,800,600' --rotation 180 --vflip
# raspistill --preview '250,250,800,600' --rotation 180 --vflip --hflip

# Camera preview
raspistill --preview '250,250,800,600' --rotation 180

# Fullscreen preview
# raspistill --fullscreen --rotation 180

# Preview with opacity
# raspistill --preview '250,250,800,600' --opacity 128 --rotation 180

# Camera preview ISO
# raspistill --preview '250,250,800,600' --ISO 100 --rotation 180
# raspistill --preview '250,250,800,600' --ISO 400 --rotation 180
# raspistill --preview '250,250,800,600' --ISO 800  --rotation 180


