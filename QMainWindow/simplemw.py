#!/usr/bin/env python3

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtWidgets import QGridLayout

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Simple Main Window")
		#button = QPushButton("Press Me!")

		# Set the central widget of the Window.
		self.cw = QWidget()
		self.setCentralWidget(self.cw)

		layout = QGridLayout()
		self.cw.setLayout(layout)

		self.label_1 = QLabel('Simple Window')
		layout.addWidget(self.label_1, 0, 0)
		self.label_2 = QLabel('Another Label')
		self.label_2.setAlignment(Qt.AlignHCenter)
		layout.addWidget(self.label_2, 1, 0)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

