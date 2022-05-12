#!/usr/bin/env python3

"""
Transverse QTreeview node and save QTreeview into dictionary

Child items for a specific item can be extracted by row index and column
index of this item. Let’s take root item from above figure as an example
it has three rows of child items and each row consists of three items.
When row index equals 0 and column index equals 0, we will get first
item of first row and retrieved data will be ‘Class 1’. When row index
equals 0 and column index equals 1, we will get null.

The same approach can be used to transverse child items of ‘Class 1’.
When row index is 1 and column index is 1, we will get 175. Row index of
1 and column index of 2 will lead to 3rd item of second row and the
value of this item is 65.

When coming to a new level of item, row index and column index will
start from 0 again. We cannot use common for loop to retrieve data of
tree again. In this case, recursive traversal should be used.
"""

import sys
from collections import deque
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class view(QWidget):
		def __init__(self, data):
				super(view, self).__init__()
				self.tree = QTreeView(self)
				layout = QVBoxLayout(self)
				layout.addWidget(self.tree)
				self.model = QStandardItemModel()
				self.model.setHorizontalHeaderLabels(['Name', 'Height', 'Weight'])
				self.tree.header().setDefaultSectionSize(180)
				self.tree.setModel(self.model)
				self.importData(data)
				self.tree.expandAll()
				tree_list = self.transverse_tree()
				print('tree_list saved from QTreeview:')
				for row in tree_list:
						print(row)
		# Function to save populate treeview with a dictionary
		def importData(self, data, root=None):
				self.model.setRowCount(0)
				if root is None:
						root = self.model.invisibleRootItem()
				seen = {}   # List of  QStandardItem
				values = deque(data)
				while values:
						value = values.popleft()
						if value['unique_id'] == 1:
								parent = root
						else:
								pid = value['parent_id']
								if pid not in seen:
										values.append(value)
										continue
								parent = seen[pid]
						unique_id = value['unique_id']
						parent.appendRow([
								QStandardItem(value['short_name']),
								QStandardItem(value['height']),
								QStandardItem(value['weight'])
						])
						seen[unique_id] = parent.child(parent.rowCount() - 1)
		# Function to transverse treeview and derive tree_list
		def transverse_tree(self):
				tree_list = []
				for i in range(self.model.rowCount()):
						item = self.model.item(i)
						level = 0
						self.GetItem(item, level, tree_list)
				return tree_list
		def GetItem(self, item, level, tree_list):
				if item != None:
						if item.hasChildren():
								level = level + 1
								short_name = ' '
								height = ' '
								weight = ' '
								id = 0
								for i in range(item.rowCount()):
										id = id + 1
										for j in reversed([0, 1, 2]):
												childitem = item.child(i, j)
												if childitem != None:
														if j == 0:
																short_name = childitem.data(0)
														else:
																short_name = short_name
														if j == 1:
																height = childitem.data(0)
														else:
																height = height
														if j == 2:
																weight = childitem.data(0)
														else:
																weight = weight
														if j == 0:
																dic = {}
																dic['level'] = level
																dic['id'] = id
																dic['short_name'] = short_name
																dic['height'] = height
																dic['weight'] = weight
																tree_list.append(dic)
														self.GetItem(childitem, level, tree_list)
								return tree_list
if __name__ == '__main__':
		data = [
				{'unique_id': 1, 'parent_id': 0, 'short_name': '', 'height': ' ', 'weight': ' '},
				{'unique_id': 2, 'parent_id': 1, 'short_name': 'Class 1', 'height': ' ', 'weight': ' '},
				{'unique_id': 3, 'parent_id': 2, 'short_name': 'Lucy', 'height': '162', 'weight': '50'},
				{'unique_id': 4, 'parent_id': 2, 'short_name': 'Joe', 'height': '175', 'weight': '65'},
				{'unique_id': 5, 'parent_id': 1, 'short_name': 'Class 2', 'height': ' ', 'weight': ' '},
				{'unique_id': 6, 'parent_id': 5, 'short_name': 'Lily', 'height': '170', 'weight': '55'},
				{'unique_id': 7, 'parent_id': 5, 'short_name': 'Tom', 'height': '180', 'weight': '75'},
				{'unique_id': 8, 'parent_id': 1, 'short_name': 'Class 3', 'height': ' ', 'weight': ' '},
				{'unique_id': 9, 'parent_id': 8, 'short_name': 'Jack', 'height': '178', 'weight': '80'},
				{'unique_id': 10, 'parent_id': 8, 'short_name': 'Tim', 'height': '172', 'weight': '60'}
		]
		app = QApplication(sys.argv)
		view = view(data)
		view.setGeometry(300, 100, 600, 300)
		view.setWindowTitle('QTreeview Example')
		view.show()
		sys.exit(app.exec_())
