#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class App(QWidget):

	def __init__(self):
		super().__init__()

		self.setWindowTitle('PyQt5 image')
		# left, top, width, height
		self.setGeometry(10, 10, 640, 480)

		# Create widget
		label = QLabel(self)
		pixmap = QPixmap('beach.png')
		label.setPixmap(pixmap)
		label.move(100,70)
		pixmapSize = pixmap.size()
		print(pixmap.size().height())
		#self.resize(pixmap.width(),pixmap.height())
		#label.setPixmap(QPixmap(icon).scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
