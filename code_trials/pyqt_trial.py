# coding=utf-8

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction,
                             QWidget, QPushButton, QMessageBox)
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtGui import QIcon


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

        GenerateMenu(self)

        self.show()

    def clicker(self):
        pop = QMessageBox.question(self, 'msg worked', 'aaaa', QMessageBox.Yes
                                   | QMessageBox.No, QMessageBox.No)
        if pop == QMessageBox.Yes:
            print('yes')
        else:
            print('no')

    @pyqtSlot(bool)
    def on_click(self):
        print('yay something worked')
        sys.exit()


class GenerateMenu:
    def __init__(self, parent):
        self.parent = parent

        self.menu_top = self.parent.menuBar()
        self.file_menu = self.menu_top.addMenu('File')
        self.edit_menu = self.menu_top.addMenu('Edit')
        self.help_menu = self.menu_top.addMenu('Help')

        # %%%%%%% add/edit material button
        self.option_new_material = QAction('Add/Edit Material', self.parent)
        self.option_new_material.setStatusTip('Add or edit a material in database')
        self.edit_menu.addAction(self.option_new_material)

        # %%%%%%%%%%%%%% exit button
        __ico_file = '/opt/google/chrome/product_logo_64.png'
        option_exit = QAction(QIcon('exit.png'), 'Exit', self.parent)
        option_exit.setShortcut('Ctrl+Q')
        option_exit.setStatusTip('Exit application')
        option_exit.triggered.connect(QCoreApplication.instance().quit)
        self.file_menu.addAction(option_exit)

        # %%%%%%%%%%%% about button
        option_about = QAction('About', self.parent)
        self.help_menu.addAction(option_about)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

