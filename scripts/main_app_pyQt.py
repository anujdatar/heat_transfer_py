# coding=utf-8

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot
from scripts.gui_files_pyqt import GenerateMenu
from scripts.gui_files_pyqt import MaterialFrame

class MainAppQt(QMainWindow):

    def __init__(self, width=1280, height=720):
        super().__init__()
        self.setWindowTitle('Heat Transfer for Selective Laser Sintering')
        self.setGeometry(50, 50, width, height)
        self.statusBar().showMessage('Welcome')
        GenerateMenu(self)

        self.x = QWidget(self)
        self.x.setGeometry(100, 100, 800, 600)

        MaterialFrame(self.x)

        # %%%%%%%%%% quit button
        button_quit = QPushButton('Quit', self)
        button_quit.setToolTip('Close Program')
        button_quit.move(600, 600)
        # button_quit.resize(100, 100)
        button_quit.clicked.connect(self.close_all)

        self.show()

    @pyqtSlot(bool)
    def close_all(self):
        print('yay something worked')
        sys.exit()


# if __name__ == '__main__':
#     app = Qtw.QApplication(sys.argv)
#     ex = MainAppQt()
#     sys.exit(app.exec_())
