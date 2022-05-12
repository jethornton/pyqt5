#!/usr/bin/env python3

"""
The three most important lines of code are:

parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)

This one sets up the parent element to be a three state check box.

child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
child.setCheckState(0, Qt.Unchecked)

These set up the child to be selectable and set the default to unchecked.
If the child's checkbox isn't given a state, the checkbox element does
not appear.
"""

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.Qt import Qt
import sys

def main(): 
	app = QtWidgets.QApplication(sys.argv)
	tree = QtWidgets.QTreeWidget()
	headerItem  = QtWidgets.QTreeWidgetItem()
	item = QtWidgets.QTreeWidgetItem()

	for i in range(3):
		parent = QtWidgets.QTreeWidgetItem(tree)
		parent.setText(0, f"Parent {i}")
		parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
		for x in range(5):
			child = QtWidgets.QTreeWidgetItem(parent)
			child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
			child.setText(0, f"Child {x}")
			child.setCheckState(0, Qt.Unchecked)
	tree.show() 
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
