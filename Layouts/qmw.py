#!/usr/bin/env python3
import sys 
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)

		exitAct = QAction(QIcon.fromTheme('application-exit'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit application')
		exitAct.triggered.connect(self.close)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAct)

		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAct)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Main window')

		self.show() 


if __name__ == "__main__": 
	app = QApplication(sys.argv) 
	ex = Example() 
	sys.exit(app.exec_())   
