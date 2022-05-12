#!/usr/bin/python3

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout
import sys


class Window(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowIcon(QIcon.fromTheme('document-open'))
		self.setWindowTitle("PyQt5 Window")
		self.setGeometry(200, 500, 400, 300)

		vbox = QVBoxLayout()

		self.btn = QPushButton("Open Second Dialog")
		self.btn.setFont(QFont("Sanserif", 15))
		self.btn.clicked.connect(self.openSecondDialog)

		vbox.addWidget(self.btn)

		self.setLayout(vbox)

		self.show()

	def openSecondDialog(self):
		mydialog = QDialog(self)
		self.closeBtn = QPushButton("Close Dialog")
		mydialog.addWidget(self.closeBtn)
		#mydialog.setModal(True)
		mydialog.exec()
		#mydialog.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
