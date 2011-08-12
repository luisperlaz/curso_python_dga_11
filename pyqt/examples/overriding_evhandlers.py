#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejemplo de sobreescritura de manejadores de eventos
'''

import sys
from PyQt4 import QtGui, QtCore

class OverrButton(QtGui.QPushButton):

    def __init__(self, txt, label2update):
        QtGui.QPushButton.__init__(self, txt)
        self.label2update = label2update

    def mousePressEvent(self, event):
        self.label2update.clear()

class OverridingEventHandlerExample(QtGui.QWidget):
  
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()
    
    def initUI(self):

        self.output = QtGui.QLabel(u"Esto se borrará al pulsar")
        self.btn = OverrButton("Pulsame!", self.output)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btn)
        vbox.addWidget(self.output)

        self.setLayout(vbox)

        self.setWindowTitle('Event handlers')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = OverridingEventHandlerExample()
ex.show()
sys.exit(app.exec_())
