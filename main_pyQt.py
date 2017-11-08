# coding=utf-8

import sys
from scripts import MainAppQt
from PyQt5 import QtWidgets as Qtw


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    ex = MainAppQt()
    sys.exit(app.exec_())
