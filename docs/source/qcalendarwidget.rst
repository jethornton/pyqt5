===============
QCalendarWidget
===============

.. py:class:: QCalendarWidget

QCalendarWidget Example

.. code-block:: python

  #!/usr/bin/python3

  import sys
  from PyQt5.QtWidgets import (QApplication, QMainWindow, QCalendarWidget,
    QWidget, QLabel, QVBoxLayout)
  from PyQt5.QtCore import QDate

  class Calendar(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setWindowTitle('Calendar')
      self.setGeometry(100,100,320,270)

      layout = QVBoxLayout()
      # set central widget
      widget = QWidget()
      widget.setLayout(layout)
      self.setCentralWidget(widget)

      self.calendar = QCalendarWidget(self)
      self.calendar.setGridVisible(True)
      self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
      self.calendar.clicked[QDate].connect(self.show_date)
      self.dateLB = QLabel(self)
      date = self.calendar.selectedDate()
      self.dateLB.setText(date.toString())
      layout.addWidget(self.calendar)
      layout.addWidget(self.dateLB)

      self.show()
    def show_date(self, date):
      self.my_label.setText(date.toString())

  app = QApplication(sys.argv)
  ex = Calendar()
  sys.exit(app.exec_())



