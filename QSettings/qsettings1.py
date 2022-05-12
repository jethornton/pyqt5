#!/usr/bin/python3

import sys, os
from PyQt5 import QtCore


settings = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
print(settings.fileName())
settings.setValue('wizardwebsshport', 8889)
#settings.setValue('theme_selection', 'Dark')
#settings.setValue('license', 'XXXXX-XXXX-XXXXX-XXXX')
#settings.remove('license')
keys = settings.allKeys()

print(keys)
