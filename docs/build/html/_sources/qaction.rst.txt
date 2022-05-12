=======
QAction
=======

.. py:class:: QAction


Check Menu
----------

.. code-block:: python

  #!/usr/bin/env python3

  import sys
  from PyQt5.QtWidgets import (QMainWindow, QAction, QApplication,
    QVBoxLayout, QWidget, QLabel)


  class CheckMenu(QMainWindow):

    def __init__(self):
      super().__init__()

      layout = QVBoxLayout()

      # set central widget
      widget = QWidget()
      widget.setLayout(layout)
      self.setCentralWidget(widget)

      self.statusbar = self.statusBar()
      self.statusbar.showMessage('Ready')

      menubar = self.menuBar()
      viewMenu = menubar.addMenu('View')

      viewStatAct = QAction('View statusbar', self, checkable=True)
      viewStatAct.setStatusTip('View statusbar')
      viewStatAct.setChecked(True)
      viewStatAct.triggered.connect(self.toggleMenu)

      viewMenu.addAction(viewStatAct)
      label = QLabel('Hover over Me')
      label.setStatusTip('Uncheck View Statusbar to Hide')
      layout.addWidget(label)

      self.setGeometry(300, 300, 300, 200)
      self.setWindowTitle('Check Menu')
      self.show()

    def toggleMenu(self, state):
      if state:
        self.statusbar.show()
      else:
        self.statusbar.hide()

  app = QApplication(sys.argv)
  ex = CheckMenu()
  sys.exit(app.exec_())

