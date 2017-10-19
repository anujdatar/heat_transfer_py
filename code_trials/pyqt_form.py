# coding=utf-8

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QAction)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class SampleMain(QMainWindow):

    def __init__(self, width=640, height=480):
        super().__init__()

        self.setGeometry(50, 50, width, height)
        self.setWindowTitle('Sample Window')
        self.setWindowIcon(QIcon('web.png'))
        self.statusBar().showMessage('Welcome')

        GenerateMenu(self)

        self.show()


class SampleForm(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent


class GenerateMenu:
    def __init__(self, parent):
        self.parent = parent

        menu_top = self.parent.menuBar()
        file_menu = menu_top.addMenu('File')
        edit_menu = menu_top.addMenu('Edit')
        help_menu = menu_top.addMenu('Help')

        # %%%%%%% add/edit material button
        option_new_material = QAction('Add/Edit Material', self.parent)
        option_new_material.setStatusTip('Add or edit a material in database')
        edit_menu.addAction(option_new_material)

        # %%%%%%%%%%%%%% exit button
        __ico_file = '/opt/google/chrome/product_logo_64.png'
        option_exit = QAction(QIcon(__ico_file), 'Exit', self.parent)
        option_exit.setShortcut('Ctrl+Q')
        option_exit.setStatusTip('Exit application')
        option_exit.triggered.connect(QCoreApplication.instance().quit)
        file_menu.addAction(option_exit)

        # %%%%%%%%%%%% about button
        option_about = QAction('About', self.parent)
        help_menu.addAction(option_about)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SampleMain()
    sys.exit(app.exec_())
