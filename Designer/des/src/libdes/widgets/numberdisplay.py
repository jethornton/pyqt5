import os

from PyQt5.QtWidgets import QApplication, QLabel

class PyNumberDisplay(QLabel):
	def __init__(self, parent=None):
		super(PyNumberDisplay, self).__init__(parent)

		

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	nd = PyNumberDisplay()
	nd.show()
	sys.exit(app.exec_())
