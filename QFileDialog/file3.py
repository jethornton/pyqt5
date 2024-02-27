from PyQt5.QtWidgets import QFileDialog

def open_file(parent):
	file_name, _ = QFileDialog.getOpenFileName(parent, 'Open file', '/home')
	if file_name:
		print(file_name)
		#f = open(file_name[0], 'r')
		#with f:
		#	data = f.read()
		#	parent.textEdit.setText(data)

