#!/usr/bin/env python3

from PyQt5 import QtCore, QtWidgets

class Widget(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Widget, self).__init__(parent)

		self.edit = QtWidgets.QTextEdit()
		btn = QtWidgets.QPushButton()
		le = QtWidgets.QLineEdit()

		lay = QtWidgets.QVBoxLayout(self)
		for w in (self.edit, btn, le):
			lay.addWidget(w)

		self.edit.viewport().installEventFilter(self)

	def eventFilter(self, obj, event):
		if obj is self.edit.viewport() and event.type() == QtCore.QEvent.MouseButtonPress:
			if event.button() == QtCore.Qt.LeftButton:
				print('test')
		return super(Widget, self).eventFilter(obj, event)

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	w = Widget()
	w.show()
	sys.exit(app.exec_())
	
