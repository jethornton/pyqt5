#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Statusbar(QMainWindow):

	def __init__(self):
		super().__init__()

		self.statusBar().showMessage('Ready')

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Statusbar')
		self.show()


app = QApplication(sys.argv)
ex = Statusbar()
sys.exit(app.exec_())
