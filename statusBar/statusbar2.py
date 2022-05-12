#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QStatusBar, QLabel, 
	QPushButton, QFrame)

class VLine(QFrame):
	# a simple VLine, like the one you get from designer
	def __init__(self):
		super().__init__()
		self.setFrameShape(self.VLine|self.Sunken)

class Statusbar(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(50, 50, 500, 300)


		self.statusBar().showMessage("bla-bla bla")
		self.lbl1 = QLabel("Label: ")
		self.lbl1.setStyleSheet('border: 0; color:  blue;')
		self.lbl2 = QLabel("Data : ")
		self.lbl2.setStyleSheet('border: 0; color:  red;')
		ed = QPushButton('StatusBar text')

		#self.statusBar().reformat()
		self.statusBar().setStyleSheet('border: 0; background-color: #FFF8DC;')
		self.statusBar().setStyleSheet("QStatusBar::item {border: none;}") 

		self.statusBar().addPermanentWidget(VLine())    # <---
		self.statusBar().addPermanentWidget(self.lbl1)
		self.statusBar().addPermanentWidget(VLine())    # <---
		self.statusBar().addPermanentWidget(self.lbl2)
		self.statusBar().addPermanentWidget(VLine())    # <---
		self.statusBar().addPermanentWidget(ed)
		self.statusBar().addPermanentWidget(VLine())    # <---

		self.lbl1.setText("Label: Hello")
		self.lbl2.setText("Data : 15-09-2019")

		ed.clicked.connect(lambda: self.statusBar().showMessage("Hello "))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Statusbar()
	window.show()
	sys.exit(app.exec_())
