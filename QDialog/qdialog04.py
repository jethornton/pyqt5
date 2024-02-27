#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PyQt5.QtWidgets import QDialogButtonBox, QVBoxLayout, QLabel

class CustomDialog(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("HELLO!")

		QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		self.layout = QVBoxLayout()
		message = QLabel("Something happened, is that OK?")
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My App")
		button = QPushButton("Press me for a dialog!")
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)
		self.show()

	def button_clicked(self, s):
		print("click", s)
		dlg = CustomDialog()
		if dlg.exec():
			print("Success!")
		else:
			print("Cancel!")

app = QApplication(sys.argv)
ex = MainWindow()
app.exec()
