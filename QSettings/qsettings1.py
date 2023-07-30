#!/usr/bin/python3

import sys, os
from PyQt5 import QtCore

# create the settings file Example-1.conf in ~/.config/QSettingsExample
settings = QtCore.QSettings('QSettingsExample', 'Example-1')
print(settings.fileName())
# settings.setValue('Section/Item', Value)
settings.setValue('nags/firmware', True)
settings.setValue('john/theme_selection', 'Dark')
settings.setValue('apple/license', 'XXXXX-XXXX-XXXXX-XXXX')
#settings.setValue('banna/firmware', True)
settings.setValue('banana/firmware', True)
# if you don't specify a section it goes in General
settings.setValue('firmware', True)
#settings.remove('license')

# force the value to be a python bool
print(settings.value('firmware', None, type=bool))

keys = settings.allKeys()


print(keys)

'''
~/.config/QSettingsExample/Example-1.conf

Note: if you change a section name the old section is not removed
unless you explicity remove it with settings.remove('section/value')

[General]
firmware=true

[apple]
license=XXXXX-XXXX-XXXXX-XXXX

[banana]
firmware=true

[banna]
firmware=true

[john]
theme_selection=Dark

[nags]
firmware=true'''
