# coding=utf-8

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QDockWidget


class VerticalSidebar(QDockWidget):
    def __init__(self, parent=None, table=None):
        super().__init__()
        self.parent = parent
        self.table_obj = table

        self.dock = QDockWidget()
        self.setFeatures(self.NoDockWidgetFeatures)
        self.setMaximumSize(30, 200)

        self.bar = SidebarButtons(self, self.table_obj)
        self.setWidget(self.bar)


class SidebarButtons(QWidget):
    def __init__(self, parent=None, table=None):
        super().__init__()
        self.parent = parent
        self.table_obj = table

        self.add_mat_button = QPushButton('+', self)
        self.add_mat_button.setGeometry(0, 0, 30, 30)
        self.add_mat_button.clicked.connect(self.add_new_row)

        self.remove_mat_button = QPushButton('-', self)
        self.remove_mat_button.setGeometry(0, 30, 30, 30)

        self.save_mats_button = QPushButton('S', self)
        self.save_mats_button.setGeometry(0, 60, 30, 30)

        self.close_button = QPushButton('C', self)
        self.close_button.setGeometry(0, 90, 30, 30)
        self.close_button.clicked.connect(sys.exit)

    def add_new_row(self):
        print('reached here')
        self.table_obj.insertRow(self.table_obj.rowCount())
