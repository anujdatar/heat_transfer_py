# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 sample')
        self.setGeometry(50, 50, 1280, 720)
        self.statusBar().showMessage('Welcome')

        self.button = QPushButton('Quit', self)
        self.button.setToolTip('Close Program')
        self.button.move(100, 100)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.on_click)

        self.button2 = QPushButton("click", self)
        self.button2.move(400, 400)
        self.button2.resize(100, 100)
        self.button2.clicked.connect(self.clicker)

        self.show()

    def clicker(self):
        pop = QMessageBox.question(self, 'msg worked', 'aaaa', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if pop == QMessageBox.Yes:
            print('yes')
        else:
            print('no')

    @pyqtSlot(bool)
    def on_click(self):
        print('yay something worked')
        sys.exit()



app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())

