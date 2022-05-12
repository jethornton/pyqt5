#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel,
	QHBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class Align(QMainWindow):
	def __init__(self):
		super().__init__()

		# set the title
		self.setWindowTitle("Label")

		# setting the geometry of window
		self.setGeometry(0, 0, 800, 100)

		# set central widget
		widget = QWidget()
		layout = QHBoxLayout()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

		# creating a label widget and setting properties
		self.label_1 = QLabel("Bottom", self)
		layout.addWidget(self.label_1)
		self.label_1.setStyleSheet("border: 1px solid black;")

		# aligning label to the bottom
		self.label_1.setAlignment(Qt.AlignBottom)

		# creating a label widget and setting properties
		self.label_2 = QLabel("Center", self)
		layout.addWidget(self.label_2)
		self.label_2.setStyleSheet("border: 1px solid black;")

		# aligning label to the center
		self.label_2.setAlignment(Qt.AlignCenter)

		# creating a label widget and setting properties
		self.label_3 = QLabel("Left", self)
		layout.addWidget(self.label_3)
		self.label_3.setStyleSheet("border: 1px solid black;")

		# aligning label to the left
		self.label_3.setAlignment(Qt.AlignLeft)

		# creating a label widget and setting properties
		self.label_4 = QLabel("Right", self)
		layout.addWidget(self.label_4)
		self.label_4.setStyleSheet("border: 1px solid black;")

		# aligning label to the right
		self.label_4.setAlignment(Qt.AlignRight)

		# creating a label widget and setting properties
		self.label_5 = QLabel("Top", self)
		layout.addWidget(self.label_5)
		self.label_5.setStyleSheet("border: 1px solid black;")

		# aligning label to the top
		self.label_5.setAlignment(Qt.AlignTop)

		# creating a label widget and setting properties
		self.label_6 = QLabel("H center", self)
		layout.addWidget(self.label_6)
		self.label_6.setStyleSheet("border: 1px solid black;")

		# aligning label to the Hcenter
		self.label_6.setAlignment(Qt.AlignHCenter)

		# creating a label widget and setting properties
		self.label_7 = QLabel("V center", self)
		layout.addWidget(self.label_7)
		self.label_7.setStyleSheet("border: 1px solid black;")

		# aligning label to the Vcenter
		self.label_7.setAlignment(Qt.AlignVCenter)

		# show all the widgets
		self.show()


# create pyqt5 app
app = QApplication(sys.argv)

# create the instance of our Window
window = Align()

# start the app
sys.exit(app.exec())

