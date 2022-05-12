#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem
 
my_app = QApplication(sys.argv)
my_window = QWidget()
my_layout = QVBoxLayout(my_window)
 
my_tree = QTreeWidget()
my_tree.setHeaderLabels(['Name', 'Cost ($)'])
my_item_root = QTreeWidgetItem(my_tree, ['Romania', '238,397 kmp'])
my_item_raw = QTreeWidgetItem(my_item_root, ['Black Sea', '436,402 kmp'])
 
my_layout.addWidget(my_tree)
my_window.show()
sys.exit(my_app.exec_())
