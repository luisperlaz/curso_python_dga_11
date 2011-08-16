#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejemplo simple de uso de signals y slots
'''

import sys
from PyQt4 import QtGui, QtCore


class SimpleSignalsSlotExample(QtGui.QWidget):
  
    def __init__(self):
        super(SimpleSignalsSlotExample, self).__init__()
        
        self.initUI()
    
    def initUI(self):

        self.btn = QtGui.QPushButton("Pulsame!")
        self.output = QtGui.QLabel(u"Esto se borrará al pulsar")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btn)
        vbox.addWidget(self.output)

        self.setLayout(vbox)
        self.connect(self.btn,  QtCore.SIGNAL('clicked()'), self.output, 
            QtCore.SLOT('clear()'))

        self.setWindowTitle('Signals y slots')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = SimpleSignalsSlotExample()
ex.show()
sys.exit(app.exec_())
