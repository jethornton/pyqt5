#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QApplication, QFileSystemModel, QTreeView,
	QWidget, QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir

class FileViewer(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle('PyQt5 File System View')
		# left, top, width, height
		self.setGeometry(0, 0, 640, 480)

		self.model = QFileSystemModel()
		self.model.setRootPath('')
		# show only directories
		self.model.setFilter(QDir.AllDirs|QDir.NoDotAndDotDot)
		self.tree = QTreeView()
		self.tree.setModel(self.model)
		# display from users home directory
		self.tree.setRootIndex(self.model.index(QDir.homePath()))

		self.tree.setIndentation(20)
		self.tree.setSortingEnabled(True)
		# sort by first column ascending, Qt.AscendingOrder = 0
		self.tree.sortByColumn(0,0)

		self.tree.setWindowTitle("Dir View")
		self.tree.resize(640, 480)
		# resize column 0 to 150 pixels wide
		self.tree.setColumnWidth(0, 150)
		self.tree.clicked.connect(self.getItem)

		windowLayout = QVBoxLayout()
		windowLayout.addWidget(self.tree)
		self.setLayout(windowLayout)

		self.show()

	def getItem(self, index):
		item = self.model.index(index.row(), 0, index.parent())
		fileName = self.model.fileName(item)
		filePath = self.model.filePath(item)
		print(f'{filePath}')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = FileViewer()
	sys.exit(app.exec_())
