#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):

    def __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        # End main UI code
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
