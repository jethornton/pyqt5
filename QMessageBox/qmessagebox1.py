#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox,
	QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
	app = QApplication(sys.argv)
	win = QWidget()
	button1 = QPushButton(win)
	button1.setText("Show dialog!")
	button1.move(50,50)
	button1.clicked.connect(showDialog)
	win.setWindowTitle("Click button")
	win.show()
	sys.exit(app.exec_())

def showDialog():
	msgBox = QMessageBox()
	chkBox = QCheckBox()
	chkBox.setText("Don't show this message again")
	msgBox.setIcon(QMessageBox.Information)
	msgBox.setText("Message box pop up window")
	msgBox.setWindowTitle("QMessageBox Example")
	msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	msgBox.setCheckBox(chkBox)
	msgBox.buttonClicked.connect(msgButtonClick)

	returnValue = msgBox.exec()
	if returnValue == QMessageBox.Ok:
		print('OK clicked')

	if returnValue == QMessageBox.Cancel:
		print('Cancel clicked')

	if chkBox.isChecked():
		print('Checked')

	if not chkBox.isChecked():
		print('Not Checked')

def msgButtonClick(i):
	print("Button clicked is:",i.text())

if __name__ == '__main__': 
	window()
