#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,  QWidget

class mainwindow(QMainWindow):
	def __init__(self):
		super().__init__()
		# left, top, width, height
		#self.setGeometry(10, 10, 300, 150)
		#self.setWindowTitle('Simple Main Window')
		self.central_widget = QWidget(self)
		self.setCentralWidget(self.central_widget)

		self.show()

app = QApplication(sys.argv)
ex = mainwindow()
sys.exit(app.exec_())

