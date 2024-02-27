#!/usr/bin/env python3

import sys

from OpenGL import GL as gl
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QOpenGLWidget


class Widget(QOpenGLWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("PyQt5, OpenGL 3.3")
		self.resize(400, 400)

	def initializeGL(self):
		gl.glClearColor(0.5, 0.5, 0.5, 1)
	
	def paintGL(self):
		gl.glClear(gl.GL_COLOR_BUFFER_BIT)


QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL)
app = QApplication(sys.argv)
w = Widget()
w.show()
sys.exit(app.exec_())

