#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QDialogButtonBox
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Simple(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Simple QDialog')
		'''
		create a QWidget and set it as the central widget on the
		QMainWindow and assign the QLayout to that. 
		You can't set a QLayout directly on the QMainWindow.
		'''
		widget = QWidget()

		# create a vertical box layout and add a couple of widgets to it
		vbox = QVBoxLayout()
		self.label1 = QLabel('Label 1')
		self.label2 = QLabel('Label 2')

		vbox.addWidget(self.label1)
		vbox.addWidget(self.label2)

		aboutBtn = QPushButton('About Dialog')
		aboutBtn.clicked.connect(self.aboutDialog)
		vbox.addWidget(aboutBtn)

		dialogBtn = QPushButton('Open Dialog')
		dialogBtn.clicked.connect(self.openDialog)
		vbox.addWidget(dialogBtn)

		closeBtn = QPushButton("Close Window")
		closeBtn.clicked.connect(self.close)
		vbox.addWidget(closeBtn)

		# set the layout to the widget
		widget.setLayout(vbox)

		# set the widget as the main window widget
		self.setCentralWidget(widget)
		self.show()

	def aboutDialog(self):
		dialogBox = QDialog()
		dialogBox.setMinimumSize(300, 300)
		dialogBox.setWindowTitle('About')

		layout = QVBoxLayout(dialogBox)


		titleLabel =  QLabel(self)
		titleLabel.setText('Mesa Configuration Tool')
		titleLabel.setAlignment(Qt.AlignCenter)
		layout.addWidget(titleLabel)

		imageLabel = QLabel(self)
		imageLabel.setAlignment(Qt.AlignCenter)

		pixmap = QPixmap('mesa.jpg')
		pixmap = pixmap.scaled(128, 128, Qt.KeepAspectRatio)
		imageLabel.setPixmap(pixmap)
		layout.addWidget(imageLabel)

		authorLabel =  QLabel(self)
		authorLabel.setText('Author: John Thornton')
		authorLabel.setAlignment(Qt.AlignCenter)
		layout.addWidget(authorLabel)


		layout.addStretch()

		buttonBox = QDialogButtonBox()
		buttonBox.setStandardButtons(QDialogButtonBox.Ok)
		buttonBox.setCenterButtons(True)
		#buttonBox.addButton("Credits", QDialogButtonBox.ActionRole)
		buttonBox.accepted.connect(dialogBox.close)
		layout.addWidget(buttonBox)

		dialogBox.exec()

	def openDialog(self):
		print('Open Dialog')
		dialogBox = QDialog()
		dialogBox.setMinimumSize(300, 300)

		self.first = QLineEdit(self)
		self.second = QLineEdit(self)

		buttonBox = QDialogButtonBox()
		buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok) 

		layout = QFormLayout(dialogBox)
		layout.addRow("First text", self.first)
		layout.addRow("Second text", self.second)
		layout.addWidget(buttonBox)

		buttonBox.accepted.connect(dialogBox.accept)
		buttonBox.rejected.connect(dialogBox.reject)

		if dialogBox.exec():
			print('Done')
			self.label1.setText(self.first.text())
			self.label2.setText(self.second.text())
		else:
			print('Canceled')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Simple()
	sys.exit(app.exec_())
