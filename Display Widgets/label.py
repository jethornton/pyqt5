#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)

class Example(QWidget):
	def __init__(self):
		super().__init__()

		# left, top, width, height
		self.setGeometry(10, 10, 300, 150)

		hbox = QHBoxLayout(self)

		lbl = QLabel(self)
		lbl.setText('QLabel')
		hbox.addWidget(lbl)
		self.setLayout(hbox)

		self.setWindowTitle('QLabel')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
