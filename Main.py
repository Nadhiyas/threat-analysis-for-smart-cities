# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 14:50
# @Author  : Jiaping Xiao
# @File    : Main.py

import sys
import widget
import PyQt4
if __name__== '__main__':
    app = widget.QtGui.QApplication(sys.argv)
    MainWindows = widget.QtGui.QMainWindow()
    ui = widget.Ui_Form()
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
