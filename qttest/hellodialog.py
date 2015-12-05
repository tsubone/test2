#!/usr/bin/env python

import sys
from PySide import QtGui
from ui_hellodialog import Ui_HelloDialog

class HelloDialog(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HelloDialog, self).__init__(parent)
        self.ui = Ui_HelloDialog ()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    dlg = HelloDialog()
    dlg.show()
    sys.exit(app.exec_())
    
