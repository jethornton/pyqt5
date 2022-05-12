#!/usr/bin/env python3

"""
Example to show and hide a QMainWindow
"""

import sys
from datetime import datetime

from pytz import timezone

from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		hideAction = QAction(QIcon.fromTheme('window-close'), 'Hide', self)
		hideAction.setShortcut('Ctrl+H')
		hideAction.setStatusTip('Hide Window')
		hideAction.triggered.connect(self.hideWindow)

		exitAction = QAction(QIcon.fromTheme('application-exit'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(self.close)

		toolbar = self.addToolBar('Hide')
		toolbar.addAction(hideAction)
		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAction)

		updateTimer = QTimer(self)
		updateTimer.timeout.connect(self.update)
		updateTimer.start(1000)

		self.hidden = 0

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Main window')
		self.show()

	def hideWindow(self):
		print('QMainWindow is Hidden')
		self.hidden = datetime.now(timezone('US/Central'))
		self.hide()

	def update(self):
		if self.isHidden():
			now = datetime.now(timezone('US/Central'))
			diff = now - self.hidden
			m, s = divmod(int(diff.total_seconds()), 60)
			h, m = divmod(m, 60)
			print(f'Seconds {s}')
			if s >= 5:
				self.show()
				print('QMainWindow is Shown')


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec_())
