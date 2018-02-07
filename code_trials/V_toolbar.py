# coding=utf-8

import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication


class MyWinow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test')
        self.setGeometry(100, 100, 200, 450)

        a = VertToolbar(self)
        layout = QVBoxLayout(self)
        layout.addWidget(a)
        self.setLayout(layout)


class VertToolbar(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.add_mat_button = QPushButton('+', self)
        self.add_mat_button.setGeometry(0, 0, 30, 30)
        self.remove_mat_button = QPushButton('-', self)
        self.remove_mat_button.setGeometry(0, 30, 30, 30)
        self.save_mats_button = QPushButton('S', self)
        self.save_mats_button.setGeometry(0, 60, 30, 30)

        self.close_button = QPushButton('C', self)
        self.close_button.setGeometry(0, 90, 30, 30)
        self.close_button.clicked.connect(sys.exit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWinow()
    w.show()
    sys.exit(app.exec_())
