#!/usr/bin/python3

"""
Create a simple QMainWindow and set the central widget

Create a QWidget and set it as the central widget on the
QMainWindow and assign the QLayout to that. 
You can't set a QLayout directly on the QMainWindow.
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMainWindow,
	QVBoxLayout, QPushButton)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Simple Main Window')

		widget = QWidget()

		# create a vertical box layout and add a couple of widgets to it
		vbox = QVBoxLayout()
		vbox.addWidget(QLabel('Test'))
		okButton = QPushButton("OK")
		okButton.clicked.connect(self.close)
		vbox.addWidget(okButton)

		# set the layout to the widget
		widget.setLayout(vbox)

		# set the widget as the main window widget
		self.setCentralWidget(widget)

		# add a toolbar button to exit the application
		exitAction = QAction(QIcon.fromTheme('application-exit'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(self.close)

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainWindow()
	sys.exit(app.exec_())
