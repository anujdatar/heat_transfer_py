# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 sample')
        self.setGeometry(50, 50, 640, 480)

        # self.statusBar().showMessage('Welcome')

        self.button = QPushButton('Quit', self)
        self.button.setToolTip('Close Program')
        self.button.move(100, 100)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.on_click)

        self.show()


    @pyqtSlot()
    def on_click(self):
        print('yay something worked')
        sys.exit()


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())

