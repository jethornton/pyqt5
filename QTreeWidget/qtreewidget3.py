#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget

if __name__ == '__main__':
	# create a empty my_app application
	my_app = ''
	# test this my_app to create instance
	if QApplication.instance() != None:
		my_app = QApplication.instance()
	else:
		my_app = QApplication(sys.argv)
	# create a QTreeWidgetItem with tree columns
	my_tree= QTreeWidgetItem(["Column A", "Column B", "Column C"])
	# add date using a for loop 
	for i in range(6):
		list_item_row = QTreeWidgetItem(["Child A-" + str(i), "Child B-" + str(i), "Child C-" + str(i)])
		my_tree.addChild(list_item_row)
	# create my_widget widget
	my_widget = QWidget()
	my_widget.resize(640, 180)
	# create a QTreeWidget named my_tree_widget 
	my_tree_widget = QTreeWidget(my_widget)
	# set the size
	my_tree_widget.resize(640, 180)
	# set the number of columns 
	my_tree_widget.setColumnCount(3)
	# add labels for each column 
	my_tree_widget.setHeaderLabels(["Column A label", "Column B label", "Column C label"])
	# add my_tree using addTopLevelItem
	my_tree_widget.addTopLevelItem(my_tree)
	# show the widget
	my_widget.show()
	# the exit of my_app
	sys.exit(my_app.exec_())
