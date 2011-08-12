#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejercicio de utilización simple de señales y slots
'''

import sys
from PyQt4 import QtGui, QtCore


class PushUpdateDial(QtGui.QWidget):
  
    def __init__(self):
        super(PushUpdateDial, self).__init__()
        self.initUI()
        self.curval = 0
    
    def update_dial(self):
        curval = self.dial.value()
        self.dial.setValue(curval + 10)

    def initUI(self):

        self.dial = QtGui.QDial()
        btn = QtGui.QPushButton("Pulsame!")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(self.dial)

        self.setLayout(vbox)
        self.connect(btn, QtCore.SIGNAL('clicked()'), self.update_dial)

        self.setWindowTitle('Signals y slots')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = PushUpdateDial()
ex.show()
sys.exit(app.exec_())
