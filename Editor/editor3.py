#!/usr/bin/python3

import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMainWindow,
	QVBoxLayout, QPushButton, QPlainTextEdit, QFileDialog, QFrame)

class VLine(QFrame):
	# a simple VLine, like the one you get from designer
	def __init__(self):
		super(VLine, self).__init__()
		self.setFrameShape(self.VLine|self.Sunken)


class jtedit(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(300, 300, 640, 480)
		self.setWindowTitle('None[*]')
		'''
		create a QWidget and set it as the central widget on the
		QMainWindow and assign the QLayout to that. 
		You can't set a QLayout directly on the QMainWindow.
		'''
		widget = QWidget()

		# create a vertical box layout and add a couple of widgets to it
		vbox = QVBoxLayout()
		self.editor = QPlainTextEdit()
		vbox.addWidget(self.editor)
		#vbox.addWidget(QLabel('Test'))
		saveBtn = QPushButton('Save')
		saveBtn.clicked.connect(self.fileSave)
		vbox.addWidget(saveBtn)

		closeBtn = QPushButton("Close")
		closeBtn.clicked.connect(self.close)
		vbox.addWidget(closeBtn)

		# set the layout to the widget
		widget.setLayout(vbox)

		# set the widget as the main window widget
		self.setCentralWidget(widget)
		self.editor.modificationChanged.connect(self.changed)
		#self.editor.textChanged.connect(self.textChanged)
		self.editor.cursorPositionChanged.connect(self.position)
		self.fileName = None
		self.csr = self.editor.textCursor()
		self.row = self.csr.blockNumber()
		self.col = self.csr.positionInBlock()
		self.statusBar()
		self.lbl1 = QLabel(f"Row:{self.row} Col:{self.col}")
		self.statusBar().addPermanentWidget(VLine())    # <---
		self.statusBar().addPermanentWidget(self.lbl1)


		self.show()

	def changed(self, is_modified):
		print('Document Modified')
		if self.fileName:
			self.setWindowTitle(f'{str(os.path.basename(self.fileName))}[*]')
		else:
			self.setWindowTitle('Modified[*]')
		self.setWindowModified(is_modified)

	def position(self):
		self.row = self.csr.blockNumber()
		self.col = self.csr.positionInBlock()
		self.lbl1.setText(f'Row:{self.row} Col:{self.col}')
		#print('Position Changed')
		#csr = self.editor.textCursor()
		#print(f'row = {csr.blockNumber()} column = {csr.positionInBlock()}')

	def textChanged(self):
		print('Text Changed')
		#self.setWindowModified(True)

	def save(self):
		print('Saved')
		self.setWindowTitle('Saved[*]')
		self.setWindowModified(False)

	def fileSave(self):
		if not self.isWindowModified(): # Nothing Changed
			self.statusBar().showMessage('Nothing Changed')
			return
		if not self.fileName: # No File Name
			self.fileSaveAs()
		else:
			with open(self.fileName, 'w') as f:
				f.write(self.editor.toPlainText())
			self.setWindowModified(False)

	def fileSaveAs(self):
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
			#self.setWindowModified(False)
			self.editor.document().setModified(False)
			self.setWindowTitle(f'{str(os.path.basename(fileName))}[*]')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = jtedit()
	sys.exit(app.exec_())
