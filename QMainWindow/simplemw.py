#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QSpinBox, QAbstractSpinBox
from PyQt5.QtGui import  QIntValidator
from PyQt5.QtCore import QLocale, Qt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Simple Main Window")
		button = QPushButton("Press Me!")

		self.cw = QWidget()
		self.setCentralWidget(self.cw)

		layout = QVBoxLayout()
		self.cw.setLayout(layout)

		only_int = QIntValidator()
		c_locale = QLocale(QLocale.C)
		only_int.setLocale(c_locale)

		self.num_le = QLineEdit()
		layout.addWidget(self.num_le)
		self.num_le.setValidator(only_int)

		self.button = QPushButton("Press Me!")
		layout.addWidget(self.button)
		self.button.clicked.connect(self.calc)

		self.spin = QSpinBox()
		self.spin.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.spin.setAlignment(Qt.AlignRight)
		layout.addWidget(self.spin)

		self.show()

	def focusInEvent(self, event):
		print('x')
		already_select_all = self.text() == self.selectedText()
		super().mousePressEvent(event)
		if not already_select_all:
			self.selectAll()


	def calc(self):
		print(int(self.num_le.text()))

app = QApplication(sys.argv)
window = MainWindow()
app.exec()

