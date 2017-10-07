# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 sample')
        self.setGeometry(50, 50, 1280, 720)
        self.statusBar().showMessage('Welcome')

        # %%%%%%%%%% menu
        generateMenu(self)

        # %%%%%%%%%% quit button
        button_quit = QPushButton('Quit', self)
        button_quit.setToolTip('Close Program')
        button_quit.move(100, 100)
        button_quit.resize(100, 100)
        button_quit.clicked.connect(self.close)

        self.show()

    @pyqtSlot(bool)
    def close_all(self):
        print('yay something worked')
        sys.exit()


class generateMenu:
    def __init__(self, parent):
        self.parent = parent

        menu_top = self.parent.menuBar()
        fileMenu = menu_top.addMenu('File')
        editMenu = menu_top.addMenu('Edit')
        helpMenu = menu_top.addMenu('Help')

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self.parent)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.parent.close)
        fileMenu.addAction(exitButton)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

