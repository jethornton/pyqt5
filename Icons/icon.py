#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

	def __init__(self):
		super().__init__()

		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Icon')

		exitAction = QAction(QIcon.fromTheme('application-exit'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)

		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAction)

		self.show()

if __name__ == "__main__": 
	app = QApplication(sys.argv) 
	ex = Example() 
	sys.exit(app.exec_())   
