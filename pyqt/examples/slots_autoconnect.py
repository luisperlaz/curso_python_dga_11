#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejemplo de autoconnect de slots
'''

import sys
from PyQt4 import QtGui, QtCore


class AutoconnectSlotsExample(QtGui.QWidget):
  
    def __init__(self):
        super(AutoconnectSlotsExample, self).__init__()
        
        self.initUI()
    
    def initUI(self):

        self.btn = QtGui.QPushButton("Pulsame!")
        self.btn.setObjectName("btn")
        self.output = QtGui.QLabel(u"Esto se borrará al pulsar")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btn)
        vbox.addWidget(self.output)

        self.setLayout(vbox)

        self.setWindowTitle('Signals y slots')
        self.resize(250, 150)
        QtCore.QMetaObject.connectSlotsByName(self)

    def on_btn_clicked(self):
        self.output.clear() 


app = QtGui.QApplication(sys.argv)
ex = AutoconnectSlotsExample()
ex.show()
sys.exit(app.exec_())
