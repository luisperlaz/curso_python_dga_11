#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
@author: Luis Pérez

Ejemplo de uso de QAction
'''

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('menubar')
        self.setCentralWidget(QtGui.QLabel(u"Prueba el menú, y usa Ctrl+Q para salir"))


        # Preparando la accion
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.svg'), 'Salir', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Salir de la aplicación')

        # Conectamos la accion
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        # La usamos en la toolbar y en el menu

        toolbar = self.addToolBar("Salir")
        toolbar.addAction(exit)
        menubar = self.menuBar()
        file = menubar.addMenu('&File') # hace que el menu file sea accesible con alt+f
        file.addAction(exit)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
