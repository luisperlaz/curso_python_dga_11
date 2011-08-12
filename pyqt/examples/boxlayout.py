#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Pérez

Ejemplo de uso de box layouts
'''

import sys
from PyQt4 import QtGui


class BoxLayoutExample(QtGui.QWidget):
  
    def __init__(self):
        super(BoxLayoutExample, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        vlayout = QtGui.QVBoxLayout()

        hlayout = QtGui.QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(okButton)
        hlayout.addWidget(cancelButton)

        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)
        
        self.setLayout(vlayout)
        self.setWindowTitle('Ejemplo de box layout')
        self.resize(400, 200)

app = QtGui.QApplication(sys.argv)
ex = BoxLayoutExample()
ex.show()
sys.exit(app.exec_())
