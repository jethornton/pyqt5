#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QListWidget, QWidget, QMessageBox, 
	QApplication, QVBoxLayout)


class Example(QWidget):

	def __init__(self):
		super().__init__()

		vbox = QVBoxLayout(self)

		listWidget = QListWidget()

		listWidget.addItem("dog") 
		listWidget.addItem("cat")
		listWidget.addItem("bird")
		listWidget.addItem("turtle")
		listWidget.addItem("you")
		listWidget.addItem("me")

		listWidget.itemDoubleClicked.connect(self.onClicked)

		vbox.addWidget(listWidget)
		self.setLayout(vbox)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('QListWidget')
		self.show()

	def onClicked(self, item):
		QMessageBox.information(self, "Info", item.text())


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
