# coding=utf-8

import sys
from PyQt5 import QtWidgets as Qtw
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(Qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 sample')
        self.setGeometry(50, 50, 1280, 720)
        self.statusBar().showMessage('Welcome')

        # %%%%%%%%%% menu
        GenerateMenu(self)

        self.main_widget = Qtw.QWidget()

        # %%%%%%% material frame
        self.material_form = Qtw.QGroupBox(
            "Material Selection", self.main_widget)
        layout = Qtw.QFormLayout(self.main_widget)
        layout.addRow(Qtw.QLabel('aaaa'), Qtw.QLineEdit())
        self.material_form.setLayout(layout)

        # %%%%%%%%%% quit button
        button_quit = Qtw.QPushButton('Quit', self)
        button_quit.setToolTip('Close Program')
        button_quit.move(500, 500)
        # button_quit.resize(100, 100)
        button_quit.clicked.connect(self.close)

        self.show()

    @pyqtSlot(bool)
    def close_all(self):
        print('yay something worked')
        sys.exit()


class GenerateMenu:
    def __init__(self, parent):
        self.parent = parent

        menu_top = self.parent.menuBar()
        file_menu = menu_top.addMenu('File')
        edit_menu = menu_top.addMenu('Edit')
        help_menu = menu_top.addMenu('Help')

        # %%%%%%% add/edit material button
        option_new_material = Qtw.QAction('Add/Edit Material', self.parent)
        option_new_material.setStatusTip('Add or edit a material in database')
        edit_menu.addAction(option_new_material)

        # %%%%%%%%%%%%%% exit button
        option_exit = Qtw.QAction(QIcon('exit24.png'), 'Exit', self.parent)
        option_exit.setShortcut('Ctrl+Q')
        option_exit.setStatusTip('Exit application')
        option_exit.triggered.connect(self.parent.close)
        file_menu.addAction(option_exit)

        # %%%%%%%%%%%% about button
        option_about = Qtw.QAction('About', self.parent)
        help_menu.addAction(option_about)


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
