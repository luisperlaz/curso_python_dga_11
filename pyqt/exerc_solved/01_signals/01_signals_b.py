#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejercicio de emision de señales propias.
'''

import sys
from PyQt4 import QtGui, QtCore


class PushUpdateDial(QtGui.QWidget):
  
    def __init__(self):
        super(PushUpdateDial, self).__init__()
        self.initUI()
        self.curval = 0
    
    def update_dial(self):
        self.curval = self.curval + 10
        self.emit(QtCore.SIGNAL("counterUpdated(int)"), self.curval)

    def initUI(self):

        dial = QtGui.QDial()
        btn = QtGui.QPushButton("Pulsame!")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(dial)

        self.setLayout(vbox)
        self.connect(btn, QtCore.SIGNAL('clicked()'), self.update_dial)
        self.connect(self, QtCore.SIGNAL('counterUpdated(int)'), dial, QtCore.SLOT("setValue(int)"))

        self.setWindowTitle('Signals y slots')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = PushUpdateDial()
ex.show()
sys.exit(app.exec_())
