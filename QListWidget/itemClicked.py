#!/usr/bin/env python3

from PyQt5.QtWidgets import (QMainWindow, QApplication, QListWidget,
	QMessageBox)
import sys
class window(QMainWindow):
	def __init__(self):
		super(window, self).__init__()
		listWidget = QListWidget()
		self.setGeometry(50, 50, 300, 200)

		listWidget.addItem("Dog")
		listWidget.addItem("Cat")
		listWidget.addItem("Bird")
		listWidget.addItem("Chicken")

		listWidget.itemClicked.connect(self.Clicked) # connect itemClicked to Clicked method

		self.setCentralWidget(listWidget)
		self.show()
        
	def Clicked(self,item):
		QMessageBox.information(self, "ListWidget", f"You clicked: {item.text()}")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = window()
	sys.exit(app.exec_())
