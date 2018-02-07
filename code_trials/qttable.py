#coding=utf-8

import sys
from PyQt5.QtWidgets import (QTableView, QWidget, QApplication,
                             QPushButton, QMainWindow, QGridLayout, QHBoxLayout,
                             QVBoxLayout)
from PyQt5.QtCore import QModelIndex, QVariant, Qt, QAbstractTableModel, QSize


table_header = ['Name', 'Density', 'Specific Heat', 'Conductivity',
                'Melting Point', 'Emissivity', 'Reflectivity']
mat_data = [['Al', 1, 2, 3, 4, 5, 6],
            ['Cu', 11, 12, 13, 14, 15, 16]]


def sample_print():
    print('testing')


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 150)

        self.child_win = None
        self.test_buttons()
        self.show()

        self.test_window()

    def test_window(self):
        self.child_win = MaterialDBWindow(self)

    def test_buttons(self):
        test_button = QPushButton('Launch Window', self)
        test_button.setGeometry(25, 50, 100, 30)
        test_button.clicked.connect(self.test_window)

        close_button = QPushButton('Close', self)
        close_button.setGeometry(125, 50, 50, 30)
        close_button.clicked.connect(sys.exit)


class MaterialDBWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setWindowTitle('Material Database')
        self.setGeometry(300, 300, 800, 600)

        self.table = MaterialTable(self)
        self.test_buttons()
        # layout = QGridLayout(self)
        # layout.addWidget(self.table, 0, 0, 10, 8)
        # layout.addWidget(self.test_button, 11, 6)
        # layout.addWidget(self.close_button, 11, 7)
        # self.setLayout(layout)

        vbox_main = QVBoxLayout(self)

        hbox_top = QHBoxLayout(self)
        hbox_top.addWidget(self.table)

        vbox_toolbar = QVBoxLayout(self)
        grid_toolbar = QGridLayout(self)
        grid_toolbar.addWidget(self.add_button, 0, 0)
        grid_toolbar.addWidget(self.add_button, 1, 0)

        vbox_toolbar.addLayout(grid_toolbar)

        hbox_top.addLayout(vbox_toolbar)

        hbox_bottom = QHBoxLayout(self)
        hbox_bottom.addWidget(self.test_button)
        hbox_bottom.addWidget(self.close_button)

        vbox_main.addLayout(hbox_top)
        vbox_main.addLayout(hbox_bottom)
        self.setLayout(vbox_main)

        self.show()

    def test_buttons(self):
        self.test_button = QPushButton('Test Print', self)
        # self.test_button.setGeometry(550, 550, 100, 30)
        self.test_button.clicked.connect(sample_print)

        self.close_button = QPushButton('Close', self)
        # self.close_button.setGeometry(675, 550, 100, 30)
        self.close_button.clicked.connect(self.close)

        self.add_button = QPushButton('+', self)
        # self.add_button.resize(50, 50)
        self.add_button.resize(5, 5)


class MaterialTable(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setGeometry(0, 0, 700, 300)

        table_model = MaterialTableModel(mat_data, table_header, self)
        test_table = QTableView()
        test_table.setModel(table_model)

        layout = QVBoxLayout(self)
        layout.addWidget(test_table)
        self.setLayout(layout)

        test_table.setShowGrid(True)
        vh = test_table.verticalHeader()
        vh.setVisible(True)
        # hh = test_table.horizontalHeader()
        # hh.setStretchLastSection(True)
        # test_table.resizeColumnsToContents()
        # test_table.resizeRowsToContents()


class MaterialTableModel(QAbstractTableModel):

    def __init__(self, datain, headerin, parent=None):
        super().__init__()

        self.array_data = datain
        self.header_data = headerin
        self.parent = parent

    def rowCount(self, parent: QModelIndex = ...):
        return len(self.array_data)

    def columnCount(self, parent: QModelIndex = ...):
        return len(self.header_data)

    def data(self, index: QModelIndex, role: int = ...):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.array_data[index.row()][index.column()])

    def headerData(self, col: int, orientation: Qt.Orientation,
                   role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header_data[col])
        return QVariant()


if __name__ == '__main__':
    wind = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(wind.exec_())
