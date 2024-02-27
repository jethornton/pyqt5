#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		textEdit = QPlainTextEdit()
		self.setCentralWidget(textEdit)

		#exitAction = QAction(QIcon.fromTheme('application-exit'), 'Exit', self)
		#exitAction.setShortcut('Ctrl+Q')
		#exitAction.setStatusTip('Exit Application')
		#exitAction.triggered.connect(self.close)

		self.statusBar()

		#menubar = self.menuBar()
		#fileMenu = menubar.addMenu('&File')
		#fileMenu.addAction(exitAction)

		#toolbar = self.addToolBar('Exit')
		#toolbar.addAction(exitAction)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Main window')
		self.show()


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec_())
