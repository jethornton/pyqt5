#!/usr/bin/python3

import sys, os

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMainWindow,
	QTextEdit, QFileDialog)

class Notepad(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('New document - Notepad Alpha[*]')
		fileMenu = self.menuBar().addMenu('File')
		saveAction = fileMenu.addAction('Save')
		saveAction.triggered.connect(self.save)
		saveAsAction = fileMenu.addAction('Save as...')
		saveAsAction.triggered.connect(self.saveAs)

		self.editor = QTextEdit()
		self.setCentralWidget(self.editor)
		self.editor.document().modificationChanged.connect(self.setWindowModified)
		self.fileName = None
		self.show()

	def save(self):
		if not self.isWindowModified():
			return
		if not self.fileName:
			self.saveAs()
		else:
			with open(self.fileName, 'w') as f:
				f.write(self.editor.toPlainText())

	def saveAs(self):
		if not self.isWindowModified():
			return
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self, 
			"Save File", "", "All Files(*);;Text Files(*.txt)", options = options)
		if fileName:
			with open(fileName, 'w') as f:
				f.write(self.editor.toPlainText())
			self.fileName = fileName
			self.setWindowTitle(str(os.path.basename(fileName)) + " - Notepad Alpha[*]")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Notepad()
	sys.exit(app.exec_())
