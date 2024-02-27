#!/usr/bin/env python3

import sys
from functools import partial

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

import file3

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		openFile = QAction(QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(partial(file3.open_file, self))

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('File dialog')
		self.show()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
