#!/usr/bin/env python3

import inspect, sys
from PyQt5 import Qt

print(f'Python {sys.version}')

vers = ['%s = %s' % (k,v) for k,v in vars(Qt).items() if k.lower().find('version') >= 0 and not inspect.isbuiltin(v)]
print('\n'.join(sorted(vers)))
