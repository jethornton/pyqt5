#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

font_button = QtGui.QFont()
font_button.setFamily("Corbel")
font_button.setPointSize(10)
font_button.setWeight(100)

class Push_button(QtWidgets.QPushButton):
	def __init__(self, parent=None):
		super(Push_button, self).__init__(parent)
		self.setMouseTracking(True)
		self.setStyleSheet("margin: 1px; padding: 10px; \
			background-color: \
			rgba(255,255,0,255); \
			color: rgba(0,0,0,255); \
			border-style: solid; \
			border-radius: 4px; border-width: 3px; \
			border-color: rgba(0,0,0,255);")

	def enterEvent(self, event):
		if self.isEnabled() is True:
			self.setStyleSheet("margin: 10px; padding: 10px; \
				background-color: \
				rgba(255,255,0,255); \
				color: rgba(0,0,10,255); \
				border-style: solid; \
				border-radius: 8px; \
				border-width: 1px; \
				border-color: \
				rgba(0,0,100,255);")
		if self.isEnabled() is False:
			self.setStyleSheet("margin: 10px; padding: 10px; \
				background-color: \
				rba(255,255,0,255); \
				color: rgba(0,0,10,255); \
				border-style: solid; \
				border-radius: 8px; \
				border-width: 1px; \
				border-color: \
				rgba(0,0,100,255);")

	def leaveEvent(self, event):
		self.setStyleSheet("margin: 10px; padding: 10px; \
			background-color: rgba(0,0,0,100); \
			color: rgba(0,0,255,255); \
			border-style: solid; \
			border-radius: 8px; border-width: 1px; \
			border-color: rgba(0,50,100,255);")


class QthreadApp(QtWidgets.QWidget):
	sig = pyqtSignal(str)
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setWindowTitle("PyQt5 style application")
		self.setWindowIcon(QtGui.QIcon("icon.png"))
		self.setMinimumWidth(int(resolution.width() / 3))
		self.setMinimumHeight(int(resolution.height() / 2))
		self.setStyleSheet("QWidget { \
			background-color: rgba(0,0,100,250);} \
			QScrollBar:horizontal {width: 1px; \
			height: 1px; \
			background-color: rgba(0,100,255,0);} \
			QScrollBar:vertical {width: 1px; \
			height: 10px; \
			background-color: rgba(0,41,59,255);}")
		self.linef = QtWidgets.QLineEdit(self)
		self.linef.setPlaceholderText("Input text ...")
		self.linef.setStyleSheet("margin: 10px; padding: 10px; \
			background-color: \
			rgba(0,0,0,255);\
			color: rgba(255,0,0,255); \
			border-style: solid; \
			border-radius: 15px; \
			border-width: 1px; \
			border-color: \
			rgba(255,255,255,255);")
		self.my_button = Push_button(self)
		self.my_button.setText("Blue")
		self.my_button.setFixedWidth(72)
		self.my_button.setFont(font_button)
		self.my_grid = QtWidgets.QGridLayout()
		self.my_grid.addWidget(self.linef, 0, 0, 1, 220)
		self.my_grid.addWidget(self.my_button, 0, 220, 1, 1)
		self.my_grid.setContentsMargins(8, 8, 8, 8)
		self.setLayout(self.my_grid)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	desktop = QtWidgets.QApplication.desktop()
	resolution = desktop.availableGeometry()
	myapp = QthreadApp()
	myapp.setWindowOpacity(0.95)
	myapp.show()
	myapp.move(resolution.center() - myapp.rect().center())
	sys.exit(app.exec_())
else:
	desktop = QtWidgets.QApplication.desktop()
	resolution = desktop.availableGeometry()
