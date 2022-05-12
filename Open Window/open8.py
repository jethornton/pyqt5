#!/usr/bin/env python3

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()                
		#self.email_blast_widget = EmailBlast()
		#self.setCentralWidget(self.email_blast_widget)
		self.welcome = OpeningWindow()
		self.setCentralWidget(self.welcome)        
		bar = self.menuBar()
		file_file = bar.addMenu('File')         
		file_edit = bar.addMenu('Edit')

	def load_email(self):
		self.mail = EmailBlast()        
		self.mail.show()
		self.welcome = OpeningWindow()
		self.destroy()

class OpeningWindow(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.welcome = QtWidgets.QLabel("Welcome To Zach's \nEmail Blast Widget")
		self.email_button = QtWidgets.QPushButton("Email")
		self.csv_button = QtWidgets.QPushButton("CSVs")
		self.exit_button = QtWidgets.QPushButton("Exit")

		self.init_ui()

def init_ui(self):
	# set layout to place widgets
	self.email_button.clicked.connect(self.load_email)
	self.csv_button.clicked.connect(self.load_csv)
	#self.exit_button.clicked.connect(self.exit)
	self.exit_button.clicked.connect(QtWidgets.qApp.quit)


class EmailBlast(QtWidgets.QWidget):
	def __init__(self):
			super().__init__()     
			# create widgets
