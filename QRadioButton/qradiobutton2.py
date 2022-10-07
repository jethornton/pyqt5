#!/usr/bin/env python3

# status: working

from PyQt5.QtWidgets import (QApplication, QWidget, QRadioButton,QHBoxLayout, QButtonGroup)
import sys

'''
Example to be able to uncheck a radio button
'''

class MainWindow(QWidget):

	def __init__(self):
		super().__init__()
		self.resize(300, 100)
		self.setWindowTitle('Radio Button')

		# Radio buttons
		self.group = QButtonGroup()
		self.group.setExclusive(False)  # Radio buttons are not exclusive
		self.group.buttonClicked.connect(self.check_buttons)

		self.b1 = QRadioButton('Radio 1')
		self.group.addButton(self.b1)

		self.b2 = QRadioButton('Radio 2')
		self.group.addButton(self.b2)

		# Layout
		self.layout = QHBoxLayout()
		self.layout.addWidget(self.b1)
		self.layout.addWidget(self.b2)
		self.setLayout(self.layout)


	def check_buttons(self, radioButton):
		# Uncheck every other button in this group
		for button in self.group.buttons():
			if button is not radioButton:
				button.setChecked(False)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()
