#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejercicio de uso de señales tipo "shortcut"
'''

import sys
from PyQt4 import QtGui, QtCore


class CustomDial(QtGui.QDial):

    def update_dial(self): 
        curval = self.value()
        self.setValue(curval + 10)


class PushUpdateDial(QtGui.QWidget):
  
    def __init__(self):
        super(PushUpdateDial, self).__init__()
        self.initUI()
    
    def update_dial(self):
        self.emit(QtCore.SIGNAL("counterUpdated"))

    def initUI(self):

        dial = CustomDial()
        btn = QtGui.QPushButton("Pulsame!")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(dial)

        self.setLayout(vbox)
        self.connect(btn, QtCore.SIGNAL('clicked()'), self.update_dial)
        self.connect(self, QtCore.SIGNAL('counterUpdated'), dial.update_dial)

        self.setWindowTitle('Signals y slots')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = PushUpdateDial()
ex.show()
sys.exit(app.exec_())
