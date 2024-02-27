#!/usr/bin/env python3

import sys, os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtGui import QPixmap

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

		dialogBtn = QPushButton('Open Dialog')
		dialogBtn.clicked.connect(self.aboutDialog)
		vbox.addWidget(dialogBtn)
		closeBtn = QPushButton("Close Window")
		closeBtn.clicked.connect(self.close)
		vbox.addWidget(closeBtn)

		# set the layout to the widget
		widget.setLayout(vbox)

		# set the widget as the main window widget
		self.setCentralWidget(widget)
		self.show()

	def accept(self):
		pass

	def reject(self):
		pass

	def aboutDialog(self):
		print('here')
		QBtn = QDialogButtonBox.Ok  # No cancel
		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		layout = QVBoxLayout()

		title = QLabel("Mozarella Ashbadger")
		font = title.font()
		font.setPointSize(20)
		title.setFont(font)

		layout.addWidget(title)

		logo = QLabel()
		logo.setPixmap( QPixmap( os.path.join('icons','ma-icon-128.png') ) )
		layout.addWidget(logo)

		layout.addWidget( QLabel("Version 23.35.211.233232") )
		layout.addWidget( QLabel("Copyright 2015 Mozarella Inc.") )

		for i in range(0, layout.count() ):
			layout.itemAt(i).setAlignment( Qt.AlignHCenter )

		layout.addWidget(self.buttonBox)

		#self.setLayout(layout)


app = QApplication(sys.argv)
ex = Simple()
sys.exit(app.exec_())
