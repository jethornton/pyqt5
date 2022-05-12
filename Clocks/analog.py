#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication)
#from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPolygon, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer, QTime, QPoint

# creating a clock class
class Clock(QMainWindow):
	def __init__(self):
		super().__init__()

		# creating a timer object
		timer = QTimer(self)

		# adding action to the timer
		# update the whole code
		timer.timeout.connect(self.update)

		# setting start time of timer i.e 1 second
		timer.start(1000)

		# setting window title
		self.setWindowTitle('Rhode Island Red Cockerel')

		# setting window geometry
		self.setGeometry(200, 200, 480, 480)

		# setting background color to the window
		self.setStyleSheet('background-image: url(rirc.jpg)')

		# creating hour hand
		self.hPointer = QPolygon([QPoint(3, 3), QPoint(-3, 3), QPoint(0, -60)])

		# creating minute hand
		self.mPointer = QPolygon([QPoint(3, 3), QPoint(-3, 3), QPoint(0, -80)])

		# creating second hand
		self.sPointer = QPolygon([QPoint(1, 1), QPoint(-1, 1), QPoint(0, -90)])

		# color for minute and hour hand
		self.bColor = Qt.green

		# color for second hand
		self.sColor = Qt.red

	# method for paint event
	def paintEvent(self, event):

		# getting minimum of width and height
		# so that clock remain square
		rec = min(self.width(), self.height())

		# getting current time
		tik = QTime.currentTime()

		# creating a painter object
		painter = QPainter(self)

		# method to draw the hands
		# argument : color rotation and which hand should be pointed
		def drawPointer(color, rotation, pointer):

			# setting brush
			painter.setBrush(QBrush(color))

			# saving painter
			painter.save()

			# rotating painter
			painter.rotate(rotation)

			# draw the polygon i.e hand
			painter.drawConvexPolygon(pointer)

			# restore the painter
			painter.restore()

		# tune up painter
		painter.setRenderHint(QPainter.Antialiasing)

		# translating the painter
		painter.translate(self.width() / 2, self.height() / 2)

		# scale the painter
		painter.scale(rec / 200, rec / 200)

		# set current pen as no pen
		painter.setPen(Qt.NoPen)

		# draw each hand
		drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
		drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
		drawPointer(self.sColor, (6 * tik.second()), self.sPointer)

		# drawing background
		painter.setPen(QPen(self.bColor))

		# for loop
		for i in range(0, 60):

			# drawing background lines
			if (i % 5) == 0:
				painter.drawLine(87, 0, 97, 0)

			# rotating the painter
			painter.rotate(6)

		# ending the painter
		painter.end()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	# creating a clock object
	win = Clock()
	# show
	win.show()
	exit(app.exec())
