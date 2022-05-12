#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import * 
 
#Main Window
class App(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('PyQt5 - QTableWidget')
		self.setGeometry(20, 20, 300, 200)

		# Create and Populate Table
		self.tableWidget = QTableWidget()

		self.tableWidget.setRowCount(4) 
		self.tableWidget.setColumnCount(2)  
		self.tableWidget.setHorizontalHeaderLabels(['Name', 'City'])
		self.tableWidget.setItem(0,0, QTableWidgetItem("Fred"))
		self.tableWidget.setItem(0,1, QTableWidgetItem("Chicago"))
		self.tableWidget.setItem(1,0, QTableWidgetItem("Alan"))
		self.tableWidget.setItem(1,1, QTableWidgetItem("Big Springs"))
		self.tableWidget.setItem(2,0, QTableWidgetItem("Ted"))
		self.tableWidget.setItem(2,1, QTableWidgetItem("Stringtown"))
		# Turn row numbers off
		self.tableWidget.verticalHeader().setVisible(False)

		# Table will fit the screen horizontally
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.horizontalHeader().setSectionResizeMode(
				QHeaderView.Stretch)

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.tableWidget)
		self.setLayout(self.layout)

		self.show()
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
