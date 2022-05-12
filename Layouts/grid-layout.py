#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

	def __init__(self):
		super().__init__()

		self.setWindowTitle('PyQt5 Grid Layout')
		# left, top, width, height
		self.setGeometry(25, 25, 380, 200)

		self.createGridLayout()

		windowLayout = QVBoxLayout()
		windowLayout.addWidget(self.horizontalGroupBox)
		self.setLayout(windowLayout)

		self.show()

	def createGridLayout(self):
		self.horizontalGroupBox = QGroupBox("Grid")
		layout = QGridLayout()
		layout.setColumnStretch(1, 4)
		layout.setColumnStretch(2, 4)

		button1 = QPushButton('1', self)
		button1.clicked.connect(self.on_click)
		button1.setObjectName('1')
		layout.addWidget(button1,0,0)

		button2 = QPushButton('2', self)
		button2.clicked.connect(self.on_click)
		button2.setObjectName('2')
		layout.addWidget(button2,0,1)

		button3 = QPushButton('3', self)
		button3.clicked.connect(self.on_click)
		button3.setObjectName('3')
		layout.addWidget(button3,0,2)


		layout.addWidget(QPushButton('1'),0,0)
		layout.addWidget(QPushButton('2'),0,1)
		layout.addWidget(QPushButton('3'),0,2)
		layout.addWidget(QPushButton('4'),1,0)
		layout.addWidget(QPushButton('5'),1,1)
		layout.addWidget(QPushButton('6'),1,2)
		layout.addWidget(QPushButton('7'),2,0)
		layout.addWidget(QPushButton('8'),2,1)
		layout.addWidget(QPushButton('9'),2,2)

		self.horizontalGroupBox.setLayout(layout)

	def on_click(self):
		#print(dir(self.sender()))
		print('PyQt5 {} button click'.format(self.sender().objectName()))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
