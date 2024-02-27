#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
 
class Communicate(QObject):
	closeApp = pyqtSignal()
 
class Example(QMainWindow):

	def __init__(self):
		super().__init__()
		self.c = Communicate()
		self.c.closeApp.connect(self.close)
		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('Mouse events') 
		self.show()
	
	def mousePressEvent(self, event):
		self.c.closeApp.emit()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
