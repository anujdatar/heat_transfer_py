# coding=utf-8

from PySide2.QtWidgets import (QTableWidget, QTableWidgetItem, QWidget,
                               QPushButton, QDockWidget, QMainWindow)
from PySide2.QtCore import Qt


class MaterialTableWidget(QTableWidget):
    def __init__(self, data, header, parent=None):
        super().__init__()
        self.parent = parent
        self.setFixedSize(742, 420)

        self.setShowGrid(True)
        self.setRowCount(len(data))
        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)

    def set_data(self, data, header):
        for i in range(len(data)):
            for j in range(len(header)):
                _new_item = str(data[i][j])
                self.setItem(i, j, QTableWidgetItem(_new_item))


class SidebarButtons(QWidget):
    def __init__(self, parent=None, table=None):
        super().__init__()
        self.parent = parent
        self.table_obj = table

        self.button_add_mat = QPushButton("+", self)
        self.button_add_mat.setGeometry(0, 0, 30, 30)
        self.button_add_mat.clicked.connect(self.add_new_row)

        self.button_remove_mat = QPushButton("-", self)
        self.button_remove_mat.setGeometry(0, 30, 30, 30)

        self.button_save_mat = QPushButton("S", self)
        self.button_save_mat.setGeometry(0, 60, 30, 30)

        self.button_close = QPushButton("Q", self)
        self.button_close.setGeometry(0, 90, 30, 30)
        self.button_close.clicked.connect(self.parent.close)

    def add_new_row(self):
        self.table_obj.insertRow(self.table_obj.rowCount())


class VerticalSidebar(QDockWidget):
    def __init__(self, parent=None, table=None):
        super().__init__()
        self.parent = parent
        self.table_obj = table

        self.setFeatures(self.NoDockWidgetFeatures)
        self.setMaximumSize(30, 200)

        self.bar = SidebarButtons(self, self.table_obj)
        self.setWidget(self.bar)



