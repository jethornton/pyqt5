#!/usr/bin/env python3

# Print Out to see designer loaded it
print("Loading Des Plugins ============================")

print('Loading Analog Clock Plugin')
from libdes.python.analogclockplugin import PyAnalogClockPlugin
print('Loading Number Display Plugin')
from libdes.python.numberplugin import PyNumberDisplayPlugin

print("Finished loading")
