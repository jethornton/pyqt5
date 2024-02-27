#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CustomDialog(QDialog):
	# Create a signal
	signal = pyqtSignal(int)

	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("Data will be lost")
		label = QLabel("Are you sure you want close the app before saving?")
		self.buttonBox = QDialogButtonBox()
		self.buttonBox.addButton(QDialogButtonBox.Save)
		self.buttonBox.addButton(QDialogButtonBox.Cancel)
		self.buttonBox.addButton(QDialogButtonBox.Close)

		layout = QVBoxLayout()
		layout.addWidget(label)
		layout.addWidget(self.buttonBox)
		self.resize(300, 100)
		self.setLayout(layout)

		# connect each button with custom slot
		self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(lambda: self.customSlot(QDialogButtonBox.Save))
		self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(lambda: self.customSlot(QDialogButtonBox.Close))
		self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(lambda: self.customSlot(QDialogButtonBox.Cancel))

		# connect signal with buil-in function from QDialog (done())
		# This done function will return <int> value and close the dialog.
		self.signal.connect(self.done)

	def customSlot(self, button_id):
		# emit button's id
		self.signal.emit(button_id)


class Window(QWidget):
	def __init__(self):
		super().__init__()
		label = QLabel('Hello Dialog', self)
		open_dialog_button = QPushButton('Open Dialog', self)
		open_dialog_button.clicked.connect(self.showDialog)

		layout = QVBoxLayout()
		layout.addWidget(label)
		layout.addWidget(open_dialog_button)
		self.setLayout(layout)

	def showDialog(self):
		dialog = CustomDialog()
		btn_clicked = dialog.exec_()  # dialog exec returns button's id

		# Now you can use the following lines of code
		if btn_clicked == QDialogButtonBox.Save:
			print("Close.. After Saving...")
		elif btn_clicked == QDialogButtonBox.Close:
			print("Close.. Without saving")
		else:
			print("Cancel.. Don't exit the program")


if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)
	win = Window()
	win.resize(200, 200)
	win.show()
	sys.exit(app.exec_())


