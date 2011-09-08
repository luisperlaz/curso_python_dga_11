#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
@author: Luis Pérez

Ejemplo de emisión de señales
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


TEMPERATURES = [u"Frío", "Templado", "Calor"] 
TEMP_COLORS = ["blue", "orange", "red"]

class TemperatureLabel(QLabel):


    def __init__(self, parent=None):
        super(TemperatureLabel, self).__init__(parent)
        self.temperature_changed(0)

    def temperature_changed(self, level):
        self.setText(u"<span style='color:{1}'>{0}</span>".format(TEMPERATURES[level], TEMP_COLORS[level]))


class EmitingSignalsExample(QDialog):


    def __init__(self, parent=None):
        super(EmitingSignalsExample, self).__init__(parent)

        self.dial = QDial()
        spinner = QSpinBox()

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        label = TemperatureLabel()
        hbox.addWidget(self.dial)
        hbox.addWidget(spinner)
        vbox.addLayout(hbox)
        vbox.addWidget(label)
        self.setLayout(vbox)

        self.connect(self.dial, SIGNAL("valueChanged(int)"), spinner.setValue)
        self.connect(spinner, SIGNAL("valueChanged(int)"), self.dial.setValue)
        self.connect(spinner, SIGNAL("valueChanged(int)"), self.emit_temperature_change)
        self.connect(self.dial, SIGNAL("temperatureChanged"), label.temperature_changed)

        self.setWindowTitle("Using default signals")
        self.resize(300, 100)

    def emit_temperature_change(self, value):

        level = min(int((float(value) / 100) * 3), 2)
        self.dial.emit(SIGNAL("temperatureChanged"), level)

        

app = QApplication(sys.argv)
dialog = EmitingSignalsExample()
dialog.show()
sys.exit(app.exec_())
