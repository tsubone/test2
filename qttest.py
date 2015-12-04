#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)
label = QLabel("<font color=red size=40>Hello world</font>");
label.show()
app.exec_()
sys.exit()
