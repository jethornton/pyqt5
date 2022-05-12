#!/usr/bin/python3

from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import QTimer

def main():
	app = QApplication([])
	mainForm = MainForm()
	mainForm.show()
	app.exec()
# end main

class MainForm(QWidget):

	def __init__(self):
		super().__init__()

		self.initUi()

		self.myDialog = MyDialog(self)
		# set that something went wrong in the dialog so it should close immediately in the showEvent
		self.myDialog.somethingWentTerriblyWrong = True
	# end function

	def initUi(self):
		# set default form size and location
		self.setGeometry(400, 400, 400, 275)

		# declare a button
		self.btnShowDialog = QPushButton('show dialog')
		self.btnShowDialog.clicked.connect(self.btnShowDialogClicked)

		# increase the font size
		setFontSize(self.btnShowDialog, 16)

		# declare a layout and add the label to the layout
		self.gridLayout = QGridLayout()
		self.gridLayout.addWidget(self.btnShowDialog)

		# add the layout to the form
		self.setLayout(self.gridLayout)
	# end function

	def btnShowDialogClicked(self):
		retVal = self.myDialog.exec()
		print('retVal = ' + str(retVal))
	# end function

# end class

class MyDialog(QDialog):

	def __init__(self, parent):
		super().__init__(parent)

		self.initUi()

		self.somethingWentTerriblyWrong = False

		self.tmrClose = QTimer(self)
		self.tmrClose.setInterval(200)
		self.tmrClose.timeout.connect(self.tmrCloseTimeout)
	# end function

	def initUi(self):
		self.setGeometry(250, 250, 250, 175)

		self.lblDialog = QLabel('label on Dialog')

		# center the label and increase the font size
		self.lblDialog.setAlignment(Qt.AlignCenter)
		setFontSize(self.lblDialog, 15)

		self.gridLayout = QGridLayout()
		self.gridLayout.addWidget(self.lblDialog)

		self.setLayout(self.gridLayout)
	# end function

	def showEvent(self, event):
		super(MyDialog, self).showEvent(event)

		# if something went terribly wrong, close this dialog form
		if self.somethingWentTerriblyWrong:
			print('in if self.somethingWentTerriblyWrong:')
			self.tmrClose.start()
		# end if
	# end function

	def tmrCloseTimeout(self):
		self.reject()
	# end function

# end class

def setFontSize(widget, fontSize):
	font = widget.font()
	font.setPointSize(fontSize)
	widget.setFont(font)
# end function

if __name__ == '__main__':
	main()
