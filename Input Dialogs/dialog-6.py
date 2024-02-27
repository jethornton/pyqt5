#!/usr/bin/env python3

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi

class LoginPage(QDialog):
	def __init__(self):
		super(LoginPage, self).__init__()
		loadUi('LoginPage.ui', self)

class RegisterPage(QDialog):
	def __init__(self):
		super(RegisterPage, self).__init__()
		loadUi('RegisterPage.ui', self)

class HomePage(QMainWindow):
	def __init__(self):
		super(HomePage, self).__init__()
		loadUi('HomePage.ui', self)
		self.btnLoginPage.clicked.connect(self.executeLoginPage)
		self.btnRegisterPage.clicked.connect(self.executeRegisterPage)

	def executeLoginPage(self):
		login_page = LoginPage()
		login_page.exec_()

	def executeRegisterPage(self):
		register_page = RegisterPage()
		register_page.exec_()

app = QApplication(sys.argv)
widget = HomePage()
widget.show()
sys.exit(app.exec_())
