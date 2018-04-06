# coding=utf-8

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from scripts.gui_files_pyqt.material_db_gui import MaterialTableWidget
from scripts.gui_files_pyqt.material_db_gui import VerticalSidebar

table_header = ['Name', 'Density', 'Specific Heat', 'Conductivity',
                'Melting Point', 'Emissivity', 'Reflectivity']
mat_data = [['Al', 1, 2, 3, 4, 5, 6],
            ['Cu', 11, 12, 13, 14, 15, 16]]


class MaterialDbWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.isWindow()
        self.parent = parent
        self.setWindowTitle('Material Database')
        # self.setGeometry(300, 300, 775, 400)
        self.setFixedSize(self.sizeHint())
        self.setWindowIcon(self.parent.logo)

        self.table = MaterialTableWidget(mat_data, table_header, self)
        self.sidebar = VerticalSidebar(self, self.table)

        self.setCentralWidget(self.table)
        self.addDockWidget(Qt.RightDockWidgetArea, self.sidebar)

        # self.sidebar.bar.add_mat_button.clicked.connect(self.add_new_material)

        self.show()

    def add_new_material(self):
        self.table.insertRow(self.table.rowCount())


class MaterialData:
    def __init__(self):
        super().__init__()

