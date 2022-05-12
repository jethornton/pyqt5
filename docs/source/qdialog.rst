=======
QDialog
=======

.. py:class:: QDialog

QDialog Example

.. code-block:: python

  #!/usr/bin/env python3

  import sys
  from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
    QDialog, QLabel, QVBoxLayout, QPushButton, QDialogButtonBox,
    QFormLayout, QLineEdit)

  class Simple(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setGeometry(300, 300, 300, 220)
      self.setWindowTitle('Simple QDialog')
      '''
      create a QWidget and set it as the central widget on the
      QMainWindow and assign the QLayout to that. 
      You can't set a QLayout directly on the QMainWindow.
      '''
      widget = QWidget()

      # create a vertical box layout and add a couple of widgets to it
      vbox = QVBoxLayout()
      self.label1 = QLabel('Label 1')
      self.label2 = QLabel('Label 2')

      vbox.addWidget(self.label1)
      vbox.addWidget(self.label2)

      dialogBtn = QPushButton('Open Dialog')
      dialogBtn.clicked.connect(self.openDialog)
      vbox.addWidget(dialogBtn)
      closeBtn = QPushButton("Close Window")
      closeBtn.clicked.connect(self.close)
      vbox.addWidget(closeBtn)

      # set the layout to the widget
      widget.setLayout(vbox)

      # set the widget as the main window widget
      self.setCentralWidget(widget)
      self.show()

    def openDialog(self):
      print('Open Dialog')
      dialogBox = QDialog()

      self.first = QLineEdit(self)
      self.second = QLineEdit(self)

      buttonBox = QDialogButtonBox()
      buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok) 

      layout = QFormLayout(dialogBox)
      layout.addRow("First text", self.first)
      layout.addRow("Second text", self.second)
      layout.addWidget(buttonBox)

      buttonBox.accepted.connect(dialogBox.accept)
      buttonBox.rejected.connect(dialogBox.reject)

      if dialogBox.exec():
        print('Done')
        self.label1.setText(self.first.text())
        self.label2.setText(self.second.text())
      else:
        print('Canceled')

  if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Simple()
    sys.exit(app.exec_())
