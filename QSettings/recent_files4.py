#!/usr/bin/env python3

import sys, os

from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, qApp
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSettings

class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()

		self.create_menus()
		self.statusBar()
		self.settings = QSettings('JT', 'recent_files')
		self.show()

	def create_menus(self):
		menubar = self.menuBar()
		new_action = QAction(QIcon.fromTheme('application-new'), '&New', self)
		open_action = QAction(QIcon.fromTheme('application-open'), '&Open', self)
		open_action.triggered.connect(self.openFile)

		exit_action = QAction(QIcon.fromTheme('application-exit'), '&Exit', self)
		exit_action.triggered.connect(qApp.quit)

		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(new_action)
		fileMenu.addAction(open_action)
		recentMenu = QMenu('Recent', self)
		fileMenu.addMenu(recentMenu)
		fileMenu.addAction(exit_action)

	def openFile(self):
		if self.settings.value('recent'):
			files = self.settings.value('recent')
		else:
			files = []
		fileName, fileFilter = QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser('~'))
		self.settings.setValue('recent', fileName)
		#print(type(fileName))
		#files.append(fileName)
		#print(type(files))
		#self.settings.setValue('recent', files)
		#print(self.settings.value('recent'))
		


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec_())
