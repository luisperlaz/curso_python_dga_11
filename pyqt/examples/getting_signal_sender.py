#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Pérez

Ejemplo de obtención del emisor de una señal
'''

import sys
from PyQt4 import QtGui, QtCore


class GettingEventSenderExample(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()

    def initUI(self):

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()

        button1 = QtGui.QPushButton("Button 1", self)
        button2 = QtGui.QPushButton("Button 2", self)
        self.output = QtGui.QLabel("")

        hbox.addWidget(button1)
        hbox.addWidget(button2)
        vbox.addLayout(hbox)
        vbox.addWidget(self.output)

        self.connect(button1, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(button2, QtCore.SIGNAL('clicked()'), self.buttonClicked)            

        self.setWindowTitle('Getting event receiver')
        self.setLayout(vbox)
        self.resize(290, 150)


    def buttonClicked(self):

        sender = self.sender()
        self.output.setText("El boton {0} ha sido pulsado".format(sender.text()))


app = QtGui.QApplication(sys.argv)
ex = GettingEventSenderExample()
ex.show()
sys.exit(app.exec_())
