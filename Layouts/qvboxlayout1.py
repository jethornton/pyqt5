#!/usr/bin/env python3

#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt


class Vertical(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Vertical Layout")
		self.setGeometry(100,100,280,360)
		layout = QVBoxLayout()

		#set spacing between your widgets
		layout.setSpacing(5)

		#set alignment in your vertical layout
		layout.setAlignment(Qt.AlignTop)

		# set central widget
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

		button1 = QPushButton('Button 1', self)
		layout.insertWidget(0, button1)

		layout.insertStretch(1)

		button2 = QPushButton('Button 2', self)
		layout.addWidget(button2)


app = QApplication(sys.argv)
main_window = Vertical()
main_window.show()
sys.exit(app.exec_())

