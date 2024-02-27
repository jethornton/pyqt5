#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QWidget,
                            QTableWidget, QTableWidgetItem,
                            QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 QTableView")
        self.setGeometry(500, 400, 500, 300)
        self.Tables()
        self.show()

    def Tables(self):
        self.tableWidget = QTableWidget()
        
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Age"))
        self.tableWidget.setItem(0, 2 , QTableWidgetItem("Gender"))
        self.tableWidget.setColumnWidth(0, 200)
 
        self.tableWidget.setItem(1,0, QTableWidgetItem("John"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("24"))
        self.tableWidget.setItem(1,2, QTableWidgetItem("Male"))
 
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Lucy"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("19"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("Female"))
 
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Subaru"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("18"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("Male"))
 
        self.tableWidget.setItem(4, 0, QTableWidgetItem("William"))
        self.tableWidget.setItem(4, 1, QTableWidgetItem("60"))
        self.tableWidget.setItem(4, 2, QTableWidgetItem("Male"))

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.tableWidget)
        self.setLayout(self.vBox)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
