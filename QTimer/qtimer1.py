#!/usr/bin/env python3

import sys
from PyQt5.QtCore import QCoreApplication, QTimer, QTime

class main(QCoreApplication):
	def __init__(self, *args, **kwargs):
		super().__init__([])

		self.timer = QTimer()
		self.time = QTime(0, 0, 0)

		self.timer.timeout.connect(self.timerEvent)
		self.timer.start(1000)
		print('Ctrl Z to quit')

	def timerEvent(self):
		self.time = self.time.addSecs(1)
		print(self.time.toString("hh:mm:ss"), end = "\r")
		#print ("\r Loading... {}".format(i)+str(i), end="")

if __name__ == '__main__':
	app = QCoreApplication(sys.argv)
	gui = main()
	sys.exit(app.exec_())


