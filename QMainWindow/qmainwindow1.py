#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

# Start the event loop.
app.exec()

