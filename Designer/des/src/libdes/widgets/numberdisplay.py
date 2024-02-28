import os

from PyQt5.QtWidgets import QApplication, QLabel
# Need direct import, designer will occasionally throw errors if you use
# QtCore.pyqtProperty still yet to figure out why...
from PyQt5.QtCore import pyqtProperty, QSize

class PyNumberDisplay(QLabel):
	def __init__(self, parent=None):
		super(PyNumberDisplay, self).__init__(parent)
		self.sometogglething = False
		self.somecountthing = 0
		self.somefloatthing = 0.0

	def minimumSizeHint(self):
		return QSize(50, 25)

	def sizeHint(self):
		return QSize(100, 25)

	def get_toggle(self):
		return self.sometogglething

	def set_toggle(self, data):
		# Sometime Validation is good here
		self.sometoggletthing = data

	# Important this goes after the functions.
	# Why I have yet to figure out it shouldn't matter
	# I really dislike inline defines like this personally
	togglething = pyqtProperty(bool, get_toggle, set_toggle)

	def get_counter(self):
		return self.somecountthing

	def set_counter(self, data):
		# Sometime Validation is good here
		self.somecountthing = data

	countthing = pyqtProperty(int, get_counter, set_counter)

	def get_floater(self):
		return self.somefloatthing

	def set_floater(self, data):
		# Sometime Validation is good here
		self.somefloatthing = data

	floatthing = pyqtProperty(float, get_floater, set_floater)

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	nd = PyNumberDisplay()
	nd.show()
	sys.exit(app.exec_())
