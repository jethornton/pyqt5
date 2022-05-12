#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class ToolBar(QMainWindow):

	def __init__(self):
		super().__init__()

		exitAct = QAction(QIcon.fromTheme('application-exit'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(qApp.quit)
		exitAct.setStatusTip('Exit application')

		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAct)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Toolbar')
		self.statusBar()

		self.show()


app = QApplication(sys.argv)
ex = ToolBar()
sys.exit(app.exec_())

