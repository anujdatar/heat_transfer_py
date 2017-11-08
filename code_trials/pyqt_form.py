# coding=utf-8

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGroupBox,
                             QGridLayout, QLineEdit, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon
from scripts.gui_files_pyqt import GenerateMenu


class SampleMain(QMainWindow):

    def __init__(self, width=640, height=480):
        super().__init__()

        self.setGeometry(50, 50, width, height)
        self.setWindowTitle('Sample Window')
        self.setWindowIcon(QIcon('web.png'))
        self.statusBar().showMessage('Welcome')
        GenerateMenu(self)

        self.form_box()

        # self.q_wid.move(100, 100)

        self.show()

    def form_box(self):

        self.q_wid = QWidget(self)
        self.q_wid.setGeometry(50, 50, 250, 250)
        self.bx_grp = QGroupBox('sample', self.q_wid)

        grid = QGridLayout(self.bx_grp)

        label_2 = QLabel('spl 2', self.bx_grp)
        entry_2 = QLineEdit(self.bx_grp)
        label_3 = QLabel('spl 2', self.bx_grp)
        entry_3 = QLineEdit(self.bx_grp)

        grid.addWidget(label_2, 0, 0)
        grid.addWidget(entry_2, 0, 1)
        grid.addWidget(label_3, 1, 0)
        grid.addWidget(entry_3, 1, 1)
        grid.addWidget(QPushButton('tttttt'), 2, 0)

        self.bx_grp.setLayout(grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SampleMain()
    sys.exit(app.exec_())
