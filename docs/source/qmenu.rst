=====
QMenu
=====

.. py:class:: QMenu

Context QMenu
-------------

.. code-block:: python

  #!/usr/bin/env python3

  import sys
  from PyQt5.QtWidgets import (QMainWindow, qApp, QMenu, QApplication,
    QVBoxLayout, QWidget, QLabel)


  class Example(QMainWindow):

    def __init__(self):
      super().__init__()

      self.setGeometry(300, 300, 300, 200)
      self.setWindowTitle('Context Menu')
      layout = QVBoxLayout()

      # set central widget
      widget = QWidget()
      widget.setLayout(layout)
      self.setCentralWidget(widget)
      label = QLabel('Right Click for Context Menu')
      layout.addWidget(label)

      self.show()

    def contextMenuEvent(self, event):
      cmenu = QMenu(self)

      newAct = cmenu.addAction("New")
      openAct = cmenu.addAction("Open")
      quitAct = cmenu.addAction("Quit")
      action = cmenu.exec_(self.mapToGlobal(event.pos()))

      if action == newAct:
        print('New Clicked')
      elif action == openAct:
        print('Open Clicked')
      elif action == quitAct:
        print('Quit Clicked')
          qApp.quit()


  app = QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())

