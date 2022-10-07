#!/usr/bin/env python3

# status: a cludge for sure

from sys import exit as sysExit
 
from PyQt5.QtCore	import *
from PyQt5.QtGui	 import *
from PyQt5.QtWidgets import *
	
class MainApp(QWidget) :
	def __init__(self,parent=None) :
# Do not use 'Super( )' unless you fully understand what it is for
# as its benefit will actually occur less often than its pitfalls	
		QWidget.__init__(self)

		# Removing this bit of useless code
		#  self.setupUi(self)

		self.pushButton_reset = QPushButton('Reset')
		self.pushButton_reset.clicked.connect(self.initialize)

		self.radioButton_degre = QRadioButton('Degrees')
		self.radioButton_degre.toggled.connect(self.display_degre_unit)

		self.radioButton_ddm = QRadioButton('DDM Units')
		self.radioButton_ddm.toggled.connect(self.display_ddm_unit)

		self.RadioGroup = QButtonGroup()
		self.RadioGroup.addButton(self.radioButton_degre)
		self.RadioGroup.addButton(self.radioButton_ddm)

		self.checkbox_confirmed = QCheckBox('Confirmed')

		HBox = QHBoxLayout()
		HBox.addWidget(self.pushButton_reset)
		HBox.addWidget(QLabel('	 '))  # Simple horizontal spacer
		HBox.addWidget(self.radioButton_degre)
		HBox.addWidget(self.radioButton_ddm)
		HBox.addWidget(QLabel('   '))  # Simple horizontal spacer
		HBox.addWidget(self.checkbox_confirmed)
		HBox.addStretch(1)

		VBox = QVBoxLayout()
		VBox.addLayout(HBox)
		VBox.addStretch(1)

		self.setLayout(VBox)

	def initialize(self):
		self.RadioGroup.setExclusive(False)

		self.radioButton_degre.setChecked(False)
		self.radioButton_ddm.setChecked(False)

		self.RadioGroup.setExclusive(True)

		self.checkbox_confirmed.setCheckState(Qt.Unchecked)

	def display_degre_unit(self):
		pass

	def display_ddm_unit(self):
		pass

if __name__=='__main__' :
	app=QApplication([])
	window=MainApp()
	window.show()
	sysExit(app.exec_())
