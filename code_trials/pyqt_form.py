# coding=utf-8

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget)
from PyQt5.QtGui import QIcon
from gui_files_pyqt import GenerateMenu


class SampleMain(QMainWindow):

    def __init__(self, width=640, height=480):
        super().__init__()

        self.setGeometry(50, 50, width, height)
        self.setWindowTitle('Sample Window')
        self.setWindowIcon(QIcon('web.png'))
        self.statusBar().showMessage('Welcome')

        GenerateMenu(self)
        SampleForm(self, x=50, y=50)

        self.show()


class SampleForm(QWidget):
    def __init__(self, parent=None, x=0, y=0):
        super().__init__()
        self.parent = parent


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    ex = SampleMain()
    # sys.exit(app.exec_())
