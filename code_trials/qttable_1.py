# coding=utf-8

import PyQt5.QtCore as QtCore
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QVBoxLayout
import sys

heading = ['Name', 'Density', 'Specific Heat', 'Conductivity',
           'Melting Point', 'Emissivity', 'Reflectivity']
data_array = [['Al', 1, 2, 3, 4, 5, 6],
              ['Cu', 11, 12, 13, 14, 15, 16]]


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setWindowTitle('Material Database')
        self.setGeometry(200, 200, 800, 600)

        table_model = MyTableModel(data_array, heading, self)
        table_view = QTableView()
        table_view.setModel(table_model)

        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None):
        super().__init__()
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent: QtCore.QModelIndex = ...):
        return len(self.arraydata)

    def columnCount(self, parent: QtCore.QModelIndex = ...):
        return len(self.headerdata)

    def data(self, index: QtCore.QModelIndex, role: int = ...):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation,
                   role: int = ...):
        if (orientation == QtCore.Qt.Horizontal and
                role == QtCore.Qt.DisplayRole):
            return QtCore.QVariant(self.headerdata[section])
        return QtCore.QVariant()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
