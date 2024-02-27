#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt5.QtGui import QFont, QTextOption
from PyQt5.QtCore import QObject

#from PyQt5.QtGui import *
class Editor(QPlainTextEdit):
	def __init__(self, parent):
		super(Editor, self).__init__()
		self.setPlainText( u'apple, banana\norange\nblah blah\n\nOh yeah!....\n'*2 )
		self.setParent( parent )
		self.setWordWrapMode( QTextOption.NoWrap )
		self.setViewportMargins( 50,0,0,0 )
		QObject.connect( self, SIGNAL("textChanged()"), self.repainting )
	def repainting(self) : self.parent().update()

class WinE(QMainWindow):
	def __init__(self, font=QFont( 'Monospace', 12 )):
		super(WinE, self).__init__()
		self.font = font
		self.font.setFixedPitch( True )
		self.ce = Editor( self )
		self.ce.setFont( self.font )
		self.setWindowTitle('Code Editor')
		self.textr = QRect( 3, 5, self.ce.childrenRect().x() -12, self.ce.childrenRect().height() )
		self.setGeometry( QRect(800, 840, 351, 250) )
		self.setCentralWidget( self.ce )
		self.show()
	def paintEvent(self, event):
		qp = QPainter   ()
		qp.begin		( self )
		self.drawLiNums ( qp )
		qp.end		  ()
	def drawLiNums(self, qp):
		qp.setPen	   ( QColor(255, 255, 255) )
		qp.setFont	  ( self.font )
		qp.drawText	 ( self.textr, Qt.AlignRight, self.lineNumeration() ) 
	def lineNumeration(self):
		return ''.join( [str(n+1) +'\n' for n in range( len(self.ce.toPlainText().splitlines(False)) )] )
def main():
	app = QApplication(sys.argv)
	ex = WinE()
	sys.exit(app.exec_())
if __name__ == '__main__': main()
