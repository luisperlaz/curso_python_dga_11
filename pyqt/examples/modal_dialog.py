#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejemplo de uso de un diálogo modal
'''

import math
import random
import string
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ModalDialogExample(QDialog):

    def __init__(self, parent=None):
        super(ModalDialogExample, self).__init__(parent)

        self.props = dict(property1="initial", property2="initial")

        self.propslabel = QLabel(str(self.props))
        changePropsButton = QPushButton("Modify properties... ")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(changePropsButton)
        layout = QVBoxLayout()
        layout.addWidget(self.propslabel)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.connect(changePropsButton, SIGNAL("clicked()"), self.open_properties_dlg)
        self.setWindowTitle("Numbers")


    def update_props_label(self):
        self.propslabel.setText(str(self.props))

    def open_properties_dlg(self):
        dialog = PropertiesDlg(self.props, self)
        res = dialog.exec_()
        if res:
            self.update_props_label()


class PropertiesDlg(QDialog):
    """Dialogo modal para modificar propiedades. Recibe las propiedades en su constructor
    y las modifica directamente cuando el dialogo se acepta."""

    def __init__(self, props, parent=None):
        super(PropertiesDlg, self).__init__(parent)

        self.props = props

        prop1Label = QLabel("Property1")
        self.prop1Edit = QLineEdit(props["property1"])
        prop1Label.setBuddy(self.prop1Edit)

        prop2Label = QLabel("Property2")
        self.prop2Edit = QLineEdit(props["property2"])
        prop2Label.setBuddy(self.prop2Edit)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok| QDialogButtonBox.Cancel)

        grid = QGridLayout()
        grid.addWidget(prop1Label, 0, 0)
        grid.addWidget(self.prop1Edit, 0, 1)
        grid.addWidget(prop2Label, 1, 0)
        grid.addWidget(self.prop2Edit, 1, 1)
        grid.addWidget(buttonBox, 2, 0, 1, 2)
        self.setLayout(grid)

        self.connect(buttonBox, SIGNAL("accepted()"), self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"), self, SLOT("reject()"))
        self.setWindowTitle("Set properties)")


    def accept(self):
        prop1value = unicode(self.prop1Edit.text())
        prop2value = unicode(self.prop2Edit.text())
        try:
            if len(prop1value) == 0:
                raise ValueError("The prop1 may not be empty.")

        except ValueError, e:
            QMessageBox.warning(self, "Validation Error", unicode(e))
            self.prop1Edit.selectAll()
            self.prop1Edit.setFocus()
            return

        self.props["property1"] = prop1value
        self.props["property2"] = prop2value
        QDialog.accept(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ModalDialogExample()
    form.show()
    app.exec_()

