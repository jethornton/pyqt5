#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QToolTip, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import pyqtSignal

class Label(QLabel):
	clicked = pyqtSignal()
	def __init__(self, parent=None):
		QLabel.__init__(self, parent=parent)

	def mousePressEvent(self, event):
		self.clicked.emit()

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.initMe()

	def initMe(self):

		label1 = QLabel(self)
		label1.setText("Überschrift mit namen des text adventure")
		label1.setStyleSheet("font-size: 18px;color: black;")
		label1.setGeometry(50, 50, 400, 100)
		label1.move(350,50)

		label2 = Label(self)
		label2.setText("Spielen")
		label2.setStyleSheet("font-size: 18px;color: black;")
		label2.setGeometry(50, 50, 400, 100)
		label2.move(450, 120)
		label2.clicked.connect(self.spielen)

		label3 = Label(self)
		label3.setText("Settings")
		label3.setStyleSheet("font-size: 18px;color: black;")
		label3.setGeometry(50, 50, 400, 100)
		label3.move(450, 200)
		label3.clicked.connect(self.settings)

		label4 = Label(self)
		label4.setText("Credits")
		label4.setStyleSheet("font-size: 18px;color: black;")
		label4.setGeometry(50, 50, 400, 100)
		label4.move(450, 280)
		label4.clicked.connect(self.credits)

		QToolTip.setFont(QFont("Arial", 10 ))
		button = QPushButton("Spiel beenden", self)
		button.setGeometry(50,50,150,50)
		button.setFont(QFont("Arial", 12))
		button.move(820, 420)
		button.setToolTip("<b>Button lel</b>")
		button.clicked.connect(self.close)
		button.clicked.connect(self.gedruekt)
		button.setStyleSheet("background-color: white;")

		self.setGeometry(50,50,1000,500)
		self.setWindowTitle("Gui lalal einhorn")
		self.setWindowIcon(QIcon("cookie.png"))
		self.setAutoFillBackground(True)
		self.setStyleSheet("background-color: lightblue;")
		self.move(500, 250)
		self.show()

	def spielen(self):
		print("spielen")

	def settings(self):
		print("settings")

	def credits(self):
		print("credits")

	def gedruekt(self):
		print("Er hats getan ;(")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = Window()
	sys.exit(app.exec_())
