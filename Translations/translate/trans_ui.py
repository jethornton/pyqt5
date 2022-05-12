# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trans.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuLanguage = QtWidgets.QMenu(self.menuEdit)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuChange_Label = QtWidgets.QMenu(self.menubar)
        self.menuChange_Label.setObjectName("menuChange_Label")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionDeutsch = QtWidgets.QAction(MainWindow)
        self.actionDeutsch.setObjectName("actionDeutsch")
        self.actionChangeLabel = QtWidgets.QAction(MainWindow)
        self.actionChangeLabel.setObjectName("actionChangeLabel")
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionDeutsch)
        self.menuEdit.addAction(self.menuLanguage.menuAction())
        self.menuChange_Label.addAction(self.actionChangeLabel)
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuChange_Label.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Load ui file"))
        self.label.setText(_translate("MainWindow", "Cats are soft"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuChange_Label.setTitle(_translate("MainWindow", "Test"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionDeutsch.setText(_translate("MainWindow", "Deutsch"))
        self.actionChangeLabel.setText(_translate("MainWindow", "Change Label"))

