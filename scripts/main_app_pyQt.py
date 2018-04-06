# coding=utf-8

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from scripts.gui_files_pyqt import MainMenu
from scripts.gui_files_pyqt import MaterialFrame
from scripts.gui_files_pyqt import ProcessFrame
from scripts.gui_files_pyqt import SolverFrame


class MainAppQt(QMainWindow):

    def __init__(self, width=1280, height=720):
        super().__init__()
        self.setWindowTitle('Heat Transfer for Selective Laser Sintering')
        self.logo = QIcon("./images/logo.png")
        self.setWindowIcon(self.logo)
        self.setGeometry(50, 50, width, height)
        self.statusBar().showMessage('Welcome')
        self.menu = MainMenu(self)
        start_x = 10
        start_y = 35
        self.materialWidget = QWidget(self)
        self.materialWidget.setGeometry(start_x, start_y, 650, 175)
        self.mat_frame = MaterialFrame(self.materialWidget)

        self.processWidget = QWidget(self)
        self.processWidget.setGeometry(start_x, start_y+175, 350, 175)
        self.proc_frame = ProcessFrame(self.processWidget)

        self.solverWidget = QWidget(self)
        self.solverWidget.setGeometry(start_x+360, start_y+175, 300, 175)
        self.solv_frame = SolverFrame(self.solverWidget)

        # %%%%%%%%%% print button
        button_print = QPushButton('Print', self)
        button_print.setToolTip('Print some stuff to console')
        button_print.setGeometry(600, 600, 100, 30)
        # button_quit.resize(100, 100)
        button_print.clicked.connect(self.print_shit)

        # %%%%%%%%%% quit button
        button_quit = QPushButton('Quit', self)
        button_quit.setToolTip('Close Program')
        button_quit.setGeometry(720, 600, 100, 30)
        # button_quit.resize(100, 100)
        button_quit.clicked.connect(self.close_all)

        self.show()

    @pyqtSlot(bool)
    def print_shit(self):
        print(self.geometry())
        print('yay something worked')

    @pyqtSlot(bool)
    def close_all(self):
        print('\n\naaaaaaa!!! Rage Quit')
        sys.exit()


# if __name__ == '__main__':
#     app = Qtw.QApplication(sys.argv)
#     ex = MainAppQt()
#     sys.exit(app.exec_())
