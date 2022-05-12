# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treewidgetwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("#centralwidget{\n"
"border: 2px solid grey;\n"
"border-radius: 5px;\n"
"padding: 5px 15px;\n"
"background-color: rgb(232, 216, 86);\n"
"}\n"
"QPushButton{\n"
"border: 2px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.985075, y2:0.017, stop:0 rgba(255, 255, 255, 255), stop:0.552239 rgba(237, 86, 0, 255));\n"
"padding: 5px 15px;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"color: rgb(238, 238, 236);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setStyleSheet("QHeaderView::section {                          \n"
"    color: black;\n"
"    padding: 2px;\n"
"    height: 20px;\n"
"    border: 5px solid black;\n"
"    border-left: 2px solid black;\n"
"    border-right:2px solid black;\n"
"}")
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 1, 1, 1, 1)
        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.gridLayout.addWidget(self.pushButton_edit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Treewidget Experiment"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Column 1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Column 2"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Column 3"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "data_01"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "data_02"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("MainWindow", "data_03"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_close.setText(_translate("MainWindow", "CLOSE"))
        self.pushButton_edit.setText(_translate("MainWindow", "EDIT"))


