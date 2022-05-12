#!/usr/bin/python3

import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMainWindow,
	QVBoxLayout, QPushButton, QAction, QFileDialog, QTextEdit)
from PyQt5.QtGui import QIcon

class Simple(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(300, 300, 640, 480)
		self.setWindowTitle('New document[*] - File Dialogs')
		'''
		create a QWidget and set it as the central widget on the
		QMainWindow and assign the QLayout to that. 
		You can't set a QLayout directly on the QMainWindow.
		'''
		widget = QWidget()

		# create a vertical box layout and add a couple of widgets to it
		vbox = QVBoxLayout()
		self.editor = QTextEdit()
		self.editor.document().modificationChanged.connect(self.mod)
		vbox.addWidget(self.editor)
		self.label = QLabel('Dialogs')
		vbox.addWidget(self.label)
		quitButton = QPushButton("Quit")
		quitButton.clicked.connect(self.close)
		vbox.addWidget(quitButton)

		# set the layout to the widget
		widget.setLayout(vbox)

		# set the widget as the main window widget
		self.setCentralWidget(widget)

		# build the Menu items
		newFile = QAction(QIcon.fromTheme('document-new'), 'New', self)
		newFile.setShortcut('Ctrl+N')
		newFile.setStatusTip('Select a File')
		newFile.triggered.connect(self.fileNew)


		openFile = QAction(QIcon.fromTheme('document-open'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Select a File')
		openFile.triggered.connect(self.fileOpen)

		openFiles = QAction(QIcon.fromTheme('document-open'), 'Open Files', self)
		openFiles.setShortcut('Ctrl+S')
		openFiles.setStatusTip('Select Multiple Files')
		openFiles.triggered.connect(self.filesOpen)

		saveFile = QAction(QIcon.fromTheme('document-save'), 'Save', self)
		saveFile.setShortcut('Ctrl+S')
		saveFile.setStatusTip('Save a File')
		saveFile.triggered.connect(self.fileSave)

		saveFileAs = QAction(QIcon.fromTheme('document-save-as'), 'Save As', self)
		saveFileAs.setShortcut('Ctrl+S')
		saveFileAs.setStatusTip('Save File As')
		saveFileAs.triggered.connect(self.fileSaveAs)

		getDirectory = QAction(QIcon.fromTheme('system-search'), 'Select a Directory', self)
		getDirectory.setShortcut('Ctrl+D')
		getDirectory.setStatusTip('Select a Directory')
		getDirectory.triggered.connect(self.directoryOpen)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(newFile)
		fileMenu.addAction(openFile)       
		fileMenu.addAction(openFiles)       
		fileMenu.addAction(saveFile)       
		fileMenu.addAction(saveFileAs)       
		fileMenu.addAction(getDirectory)       

		self.fileName = None
		self.statusBar()
		self.show()

	def mod(self):
		if self.fileName:
			self.setWindowTitle(f'{str(os.path.basename(self.fileName))}[*]')
		else:
			self.setWindowTitle('New document[*]')
		self.setWindowModified(True)


	def fileNew(self):
		pass

	def fileOpen(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.fileName, _ = QFileDialog.getOpenFileName(self, \
			"QFileDialog.getOpenFileName()", "", \
			"All Files (*);;Python Files (*.py)", options=options)
		if self.fileName:
			path, name = os.path.split(self.fileName)
			self.label.setText(f'Path\n{path}\n\nFile Name\n{name}')
			text = open(self.fileName).read()
			self.editor.setPlainText(text)
			self.setWindowTitle(f'{name}[*]')
			self.setWindowModified(False)
			#self.editor.document().setModified(False)

	def filesOpen(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		files, _ = QFileDialog.getOpenFileNames(self, \
			"QFileDialog.getOpenFileNames()", \
			"","All Files (*);;Python Files (*.py)", options=options)
		if files:
			for file in files:
				print(file)

	def fileSave(self):
		if not self.isWindowModified(): # Nothing Changed
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
			self.setWindowModified(False)
			self.editor.document().setModified(False)
			self.setWindowTitle(f'{str(os.path.basename(fileName))}[*] - File Dialogs')

	def directoryOpen(self):
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Simple()
	sys.exit(app.exec_())
