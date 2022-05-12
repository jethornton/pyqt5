#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, qApp, QApplication
from PyQt5.QtGui import QIcon

class SubMenu(QMainWindow):

	def __init__(self):
		super().__init__()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('File')

		newAct = QAction(QIcon.fromTheme('document-new'), '&New', self)
		newAct.setShortcut('Ctrl+N')
		newAct.setStatusTip('New Something')
		newAct.triggered.connect(self.new)

		exitAct = QAction(QIcon.fromTheme('application-exit'), '&Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit application')
		exitAct.triggered.connect(qApp.quit)

		mailMenu = QMenu('Mail', self)
		mailAct = QAction(QIcon.fromTheme('mail-send-receive'),'Import mail', self)
		mailMenu.addAction(mailAct)
		mailAct.triggered.connect(self.getMail)


		fileMenu.addAction(newAct)
		fileMenu.addMenu(mailMenu)
		fileMenu.addAction(exitAct)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Submenu')
		self.show()

	def new(self):
		print('New Something')

	def getMail(self):
		print('Getting Mail')

app = QApplication(sys.argv)
ex = SubMenu()
sys.exit(app.exec_())


