#!/usr/bin/env python3

from PyQt5.QtWidgets import (
	QApplication,
	QMainWindow,
	QDialog,
	QWidget,
	QVBoxLayout,
	QLineEdit,
	QLabel,
	QPushButton
	)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.user_input = QLineEdit()
		self.populate()
		self.show()

	def populate(self):
		widgets = [QLabel("Insert a number"), self.user_input]
		centralWidget = self.group_widgets(widgets)
		self.setCentralWidget(centralWidget)

	def group_widgets(self, widgets):
		parentWidget = QWidget()
		layout = QVBoxLayout()
		for widget in widgets: layout.addWidget(widget)
		parentWidget.setLayout(layout)
		return parentWidget

	def when_input(self, function):
		self.user_input.textChanged.connect(function)

class Dialog(QDialog):
	def __init__(self):
		super().__init__()
		self.user_input = QLineEdit()
		self.admin_input = QLineEdit("0")
		self.button = QPushButton("add")
		self.relay_sum = None  # function to relay result of addition
		self.populate()
		self.show()

	def populate(self):
		widgets = self.get_widgets()
		layout = self.get_layout(widgets)
		self.setLayout(layout)

	def get_widgets(self):
		widgets = [
			QLabel("Inserted number"),
			self.user_input,
			QLabel("Insert the second number"),
			self.admin_input,
			self.button
			]
		return widgets

	def get_layout(self, widgets):
		layout = QVBoxLayout()
		for widget in widgets: layout.addWidget(widget)
		return layout

	def when_buttonReleased(self, function):
		self.relay_sum = function
		self.button.released.connect(self.process_input)

	def process_input(self):
		user_number = float(self.user_input.text())
		admin_number = float(self.admin_input.text())
		result = "%.2f" %(user_number + admin_number)
		self.relay_sum(result)

def main():
	app = QApplication([])
	mainWindow = MainWindow()
	dialog = Dialog()
	mainWindow.when_input(lambda text: dialog.user_input.setText(text))
	dialog.when_buttonReleased(lambda text: mainWindow.user_input.setText(text))
	app.exec_()

if __name__ == "__main__":
	main()
