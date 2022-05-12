#!/usr/bin/python3

import os, sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPlainTextEdit,
	QShortcut)
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtCore


class MyTextEdit(QPlainTextEdit):  
	def __init__(self):
		QPlainTextEdit.__init__(self)     

		self.modificationChanged.connect(self.on_change)
		self.save_seq = QShortcut(QKeySequence('Ctrl+S'), self)
		self.save_seq.activated.connect(self.save)

		self.quitSc = QShortcut(QKeySequence('Ctrl+Q'), self)
		self.quitSc.activated.connect(QApplication.instance().quit)

	def on_change(self, is_modified):
		print( "on_change")
		window.setWindowModified(is_modified)

	def save(self):
		print('Saved')
		window.setWindowModified(False)



app = QApplication(sys.argv)
window = QMainWindow()
edit = MyTextEdit()
window.setCentralWidget(edit)
window.setWindowTitle("None [*]")
window.show()
app.exec_()
