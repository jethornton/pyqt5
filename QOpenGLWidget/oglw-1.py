#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class mainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		loadUi('oglw-1.ui', self)

		self.openGLWidget.initializeGL = self.initializeGL
		self.openGLWidget.resizeGL = self.resizeGL
		self.openGLWidget.paintGL = self.paintGL

		''' If you need to trigger a repaint from places other than paintGL() 
		(a typical example is when using timers to animate scenes), you should call
		the widget’s update() function to schedule an update. '''
		#timer = QTimer(self)
		#timer.timeout.connect(self.openGLWidget.update) 
		#timer.start(1000)

		self.lastPos = QPoint()
		self.xRot = 0
		self.yRot = 0
		self.zRot = 0

	def initializeGL(self):
		pass
		#print('init')

	def paintGL(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1,0,0);
		glBegin(GL_LINES);
		glVertex3f(0,0,0);
		glVertex3f(1,0,0);
		glVertex3f(1,1,0);
		glVertex3f(1,1,1);
		glVertex3f(0,1,1);
		#glVertex3f(5.0,0.5,0);
		#glVertex3f(0.0,0.5,1);
		glEnd()

		'''
		void gluPerspective(GLdouble fovy, GLdouble aspect, GLdouble zNear,
		GLdouble zFar);
		fovy Specifies the field of view angle, in degrees, in the y direction. 
		aspect Specifies the aspect ratio that determines the field of view in the 
		x direction. The aspect ratio is the ratio of x (width) to y (height). 
		zNear Specifies the distance from the viewer to the near clipping plane
		(always positive). 
		zFar Specifies the distance from the viewer to the far clipping plane
		(always positive). 
		'''
		gluPerspective(45, 651/551, 0.1, 50.0)
		'''
		void glTranslatef(GLfloat x, GLfloat y, GLfloat z);
		'''
		glTranslatef(0.0, 0.0, -0.5)

	def resizeGL(self, width, height):
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		#gluPerspective(40.0, 1.0, 1.0, 30.0)

	def mousePressEvent(self, event):
		self.lastPos = event.pos()

	def mouseMoveEvent(self, event):
		dx = event.x() - self.lastPos.x()
		dy = event.y() - self.lastPos.y()

		if event.buttons() & Qt.LeftButton:
			self.setXRotation(self.xRot + 8 * dy)
			self.setYRotation(self.yRot + 8 * dx)
		elif event.buttons() & Qt.RightButton:
			self.setXRotation(self.xRot + 8 * dy)
			self.setZRotation(self.zRot + 8 * dx)

		self.lastPos = event.pos()

	def setXRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.xRot:
			self.xRot = angle
			self.update()

	def setYRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.yRot:
			self.yRot = angle
			self.update()

	def setZRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.zRot:
			self.zRot = angle
			self.update()

	def normalizeAngle(self, angle):
		while angle < 0:
			angle += 360 * 16
		while angle > 360 * 16:
			angle -= 360 * 16
		return angle


app = QApplication(sys.argv)
window = mainWindow()
window.show()
sys.exit(app.exec_())
