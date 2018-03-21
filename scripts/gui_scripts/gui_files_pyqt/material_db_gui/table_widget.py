# coding=utf-8

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class MaterialTableWidget(QTableWidget):
    def __init__(self, data, header, parent=None):
        super().__init__()
        self.parent = parent
        self.setFixedSize(742, 420)

        self.setShowGrid(True)
        self.setRowCount(len(data))
        self.setColumnCount(len(header))
        self.setHorizontalHeaderLabels(header)

        self.set_data(data, header)

    def set_data(self, data, header):
        for i in range(len(data)):
            for j in range(len(header)):
                _new_item = str(data[i][j])
                self.setItem(i, j, QTableWidgetItem(_new_item))
