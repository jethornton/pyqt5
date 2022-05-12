#!/usr/bin/env python3

"""
Add styles into QTreeview

There is no method to set style for a whole row and the only way is to
customize item one by one. Thus, recursive traversal introduced should
be used here.
"""

import sys
from collections import deque
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
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
						# Add style to tree rows
						item = self.model.item(0)
						for i in range(item.rowCount()):
								for j in range(7):
										childitem = item.child(i, j)
										if childitem != None:
												childitem.setBackground(QColor(225, 225, 225))
												childitem.setSizeHint(QSize(30, 25))
												childitem.setTextAlignment(Qt.AlignBottom)
												childitem.setFont(QFont("Times New Roman", weight=QFont.Bold))
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
