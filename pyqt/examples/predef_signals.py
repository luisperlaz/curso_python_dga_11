#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Luis Pérez

Ejemplo de conexión de señales y slots de qt por defecto que se pasan parámetros
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DefaultSignalsExample(QDialog):

    def __init__(self, parent=None):
        super(DefaultSignalsExample, self).__init__(parent)

        dial = QDial()
        spinner = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinner)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), spinner.setValue)
        self.connect(spinner, SIGNAL("valueChanged(int)"), dial.setValue)

        # Equivalente 
        #self.connect(dial, SIGNAL("valueChanged(int)"), spinner, SLOT("setValue(int)"))
        #self.connect(spinner, SIGNAL("valueChanged(int)"), dial, SLOT("setValue(int)"))

        self.setWindowTitle("Using default signals")
        self.resize(300, 200)

app = QApplication(sys.argv)
dialog = DefaultSignalsExample()
dialog.show()
sys.exit(app.exec_())
