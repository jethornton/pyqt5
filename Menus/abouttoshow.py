#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
'''
When the contents of a menu are dynamic, I usually prefer to use the aboutToShow
signal of QMenu, which is triggered right before it's going to be opened, and
connect to a function that clears it and updates its contents.

I also use QAction.setData to store the file name, which allows to show a
customized text (for example, if the path is too long, we can elide it, or show
the file name only instead of the full path).
'''

class Application(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(Application, self).__init__(*args, **kwargs)

		file_menu = self.menuBar().addMenu('&File')
		self.recent_menu = file_menu.addMenu('&Open recent')

		self.recent_menu.aboutToShow.connect(self.update_recent_menu)
		self.recent_menu.triggered.connect(self.open_file_from_recent)
		self.settings = {}
		self.show()

	def update_recent_menu(self):
		self.recent_menu.clear()
		for row, filename in enumerate(self.get_recent_files(), 1):
			recent_action = self.recent_menu.addAction('&{}. {}'.format(
				row, filename))
			recent_action.setData(filename)

	def get_recent_files(self):
		recent = self.settings.get('recent files')
		if not recent:
			# just for testing purposes
			recent = self.settings['recent files'] = ['filename 4', 'filename1', 'filename2', 'filename3']
		return recent

	def open_file_from_recent(self, action):
		self.open_file(action.data())

	def open_file(self, filename):
		recent = self.get_recent_files()
		if filename in recent:
			recent.remove(filename)
		recent.insert(0, filename)

		print(filename)

app = QApplication(sys.argv)
ex = Application()
sys.exit(app.exec_())
