#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])
window = QWidget(windowTitle='Hello Qt')
window.show()
app.exec()
