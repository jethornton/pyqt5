#!/usr/bin/env python3

import sys
from array import array
from PyQt5 import QtCore, QtWidgets, uic
import pyqtgraph.opengl as gl

class app_1(QtWidgets.QDialog):
    def __init__(self):
        super(app_1,self).__init__()
        uic.loadUi('ogl-2.ui', self)
        self.setWindowTitle('Test GL app')
        self.pushButton.clicked.connect(self.on_push_b1)
        axis = gl.GLAxisItem()
        self.openGLWidget.addItem(axis)
        text = gl.GLTextItem()
        p = array('d',[0,0,0])
        t = 'TEST'
        text.setData(pos=p, text=t)
        self.openGLWidget.addItem(text)

    #@QtCore.pyqtSlot()
    def on_push_b1(self):
        axis = gl.GLAxisItem(x=10, y=30, z=50)
        self.openGLWidget.addItem(axis)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wid=app_1()
    wid.show()
    sys.exit(app.exec_())
