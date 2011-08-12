#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejemplo de GridLayout
'''

import sys
from PyQt4 import QtGui


class GridLayoutEx(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.initUI()

    def initUI(self):

        self.setWindowTitle('Ejemplo de grid layout')
        names = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '', '0', '']

        grid = QtGui.QGridLayout()
        for i in range(0,3):
            for j in range(0,3):
                name = names[i * 3 + j]
                if name == '':
                    grid.addWidget(QtGui.QLabel(''), 0, 2)
                else: 
                    button = QtGui.QPushButton(name)
                    grid.addWidget(button, i, j)

        self.setLayout(grid)


app = QtGui.QApplication(sys.argv)
widg = GridLayoutEx()
widg.show()
sys.exit(app.exec_())

