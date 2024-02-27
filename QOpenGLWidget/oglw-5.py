#!/usr/bin/env python3

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QOpenGLShader, QOpenGLShaderProgram, QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget


class OpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.shaderProgram = None

    def initializeGL(self):
        #self.initializeOpenGLFunctions()

        vertexShaderSource = """
            attribute vec2 position;
            void main() {
                gl_Position = vec4(position, 0.0, 1.0);
            }
        """

        fragmentShaderSource = """
            void main() {
                gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
            }
        """

        vertexShader = QOpenGLShader(QOpenGLShader.Vertex, self)
        vertexShader.compileSourceCode(vertexShaderSource)

        fragmentShader = QOpenGLShader(QOpenGLShader.Fragment, self)
        fragmentShader.compileSourceCode(fragmentShaderSource)

        self.shaderProgram = QOpenGLShaderProgram(self)
        self.shaderProgram.addShader(vertexShader)
        self.shaderProgram.addShader(fragmentShader)
        self.shaderProgram.link()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.shaderProgram.bind()
        vertices = [-0.5, -0.5, 0.5, -0.5, 0.0, 0.5]
        self.shaderProgram.setAttributeArray(
            "position", vertices, 2)
        self.shaderProgram.enableAttributeArray("position")
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Python Qt OpenGL Example")

        self.widget = OpenGLWidget(self)
        self.setCentralWidget(self.widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    format = QSurfaceFormat()
    format.setVersion(2, 1)
    format.setProfile(QSurfaceFormat.CoreProfile)
    QSurfaceFormat.setDefaultFormat(format)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
