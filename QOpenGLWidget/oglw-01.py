#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class mainWindow(QMainWindow):	#Main class.
	
	verticies = (
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1)
	)

	edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
	)

	colors = (
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,1,0),
	(1,1,1),
	(0,1,1),
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(1,0,0),
	(1,1,1),
	(0,1,1),
	)

	surfaces = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6)
	)

	def __init__(self):
		super(mainWindow, self).__init__()
		self.width = 700	#Variables used for the setting of the size of everything
		self.height = 600
		self.setGeometry(0, 0, self.width, self.height)	#Set the window size

	def setupUI(self):
		self.openGLWidget = QOpenGLWidget(self)	#Create the GLWidget
		self.openGLWidget.setGeometry(0, 0, self.width, self.height)	#Size it the same as the window.
		self.openGLWidget.initializeGL()
		self.openGLWidget.resizeGL(self.width, self.height)	#Resize GL's knowledge of the window to match the physical size?
		self.openGLWidget.paintGL = self.paintGL	#override the default function with my own?

	def paintGL(self):
		glLoadIdentity()
		gluPerspective(45, self.width / self.height, 0.1, 50.0)	#set perspective?
		glTranslatef(0, 0, -10)	#I used -10 instead of -2 in the PyGame version.
		glRotatef(-90, 1, 0, 0)	#I used 2 instead of 1 in the PyGame version.

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)	#Straight from the PyGame version, with 'self' inserted occasionally

		'''
		glBegin(GL_QUADS)	#tell GL to draw surfaces
		for surface in self.surfaces:
			x = 0
			for vertex in surface:
				x+=1
				glColor3fv(self.colors[x])
				glVertex3fv(self.verticies[vertex])
		glEnd()	#tell GL to stop drawing surfaces
		'''
		glBegin(GL_LINES) #tell GL to draw lines
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.verticies[vertex])
		glEnd()	#tell GL to stop drawing lines.

app = QApplication([])
window = mainWindow()
window.setupUI()
window.show()
sys.exit(app.exec_())
