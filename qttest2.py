#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *

def sayHello():
    print "Hello World!"

app = QApplication (sys.argv)
button = QPushButton ("Click me")
button.clicked.connect (sayHello)
button.show()

app.exec_()

