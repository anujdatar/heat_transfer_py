# codimg=utf-8

import sys
from PySide2.QtWidgets import QAction


class MainMenu:

    def __init__(self, parent):
        self.parent = parent

        # defining main menu items
        self.menu_bar = self.parent.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.material_menu = self.menu_bar.addMenu("Materials")
        self.help_menu = self.menu_bar.addMenu("Help")

        # %%%%%% launch material database button
        self.open_materialDB = QAction("Open Material Database", self.parent)
        self.material_menu.addAction(self.open_materialDB)

        # %%%%%% exit button
        exit_application = QAction("Exit", self.parent)
        self.file_menu.addAction(exit_application)
        exit_application.triggered.connect(sys.exit)

        # %%%%%% about button
        about_menu_option = QAction("About", self.parent)
        self.help_menu.addAction(about_menu_option)
