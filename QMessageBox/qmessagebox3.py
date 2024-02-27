#!/usr/bin/env python3

# BROKEN

class MainWindow:
	def __init__(self):

		self.ignorePopups = []
	
	def popupInfo(self, page, msg1, msg2):
		if page in self.ignorePopups:
			return

		retval = msg.exec_()
		if retval and cb.isChecked():
			self.ignorePopups.append(page)

	def show1(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.page)
		self.popupInfo(self.ui.page, "aaa", "bbb")

	def show2(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
		self.popupInfo(self.ui.page_2, "aaa", "bbb")


# create the dialog with a parent, which will make it *modal*
	mb = qtw.QMessageBox(self)
	mb.setWindowTitle('Close application') 
	mb.setText('Do you really want to quit?') 
	# you can set the text on a checkbox directly from its constructor
	cb = qtw.QCheckBox("Don't show this message again")
	mb.setCheckBox(cb)
	mb.setStandardButtons(mb.Yes | mb.No)
	ret = mb.exec_()
	# call some function that stores the checkbox state
	self.storeCloseWarning(cb.isChecked())
	if ret == mb.No:
		return
	self.close()
