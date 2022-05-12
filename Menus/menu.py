#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

"""
QMainWindow includes a menu bar, a tool bar and a status bar
"""

class Menu(QMainWindow):

	def __init__(self):
		super().__init__()

		newAct = QAction(QIcon.fromTheme('application-new'), '&New', self)
		newAct.setShortcut('Ctrl+N')
		newAct.setStatusTip('New Something')
		newAct.triggered.connect(self.new)

		exitAct = QAction(QIcon.fromTheme('application-exit'), '&Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit application')
		exitAct.triggered.connect(qApp.quit)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(newAct)
		fileMenu.addAction(exitAct)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Menu')
		self.show()

	def new(self):
		print('New Something')

app = QApplication(sys.argv)
ex = Menu()
sys.exit(app.exec_())



