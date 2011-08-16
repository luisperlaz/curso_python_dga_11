#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Luis Pérez

Ejemplo de uso de form layout
'''

from PyQt4 import QtCore, QtGui

class FormLayoutExample(QtGui.QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(FormLayoutExample, self).__init__()

        layout = QtGui.QFormLayout()
        layout.addRow(QtGui.QLabel("Field 1:"), QtGui.QLineEdit())
        layout.addRow(QtGui.QLabel("Combo 2, long text:"), QtGui.QComboBox())
        layout.addRow(QtGui.QLabel("Control 3:"), QtGui.QSpinBox())

        self.setLayout(layout)
        self.setWindowTitle("Form Layout")

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = FormLayoutExample()
    sys.exit(dialog.exec_())
