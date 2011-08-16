#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejercicio de creación de una calculadora simple usando PyQt.
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from calculator_window import Ui_MainWindow

class CalculatorDialog(QMainWindow):

    def __init__(self, parent=None):
        super(CalculatorDialog, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.prepare_connections()

    def prepare_connections(self):
        for num in range(0,10):
            btn = self.ui.__dict__['button_' + str(num)]
            self.connect(btn, SIGNAL("clicked()"), self.digit_pressed)

        for op in ["Plus", "Minus", "Mult", "Div"]:
            btn = self.ui.__dict__['button' + op]
            self.connect(btn, SIGNAL("clicked()"), self.operator_pressed)


    def digit_pressed(self):
        pressedBtn = self.sender()
        self.handle_digit(pressedBtn.text())

    def operator_pressed(self):
        pressedBtn = self.sender()
        self.handle_operator(pressedBtn.text())

    def on_buttonCE_clicked(self):
        self.ui.display.setText("")

    def on_buttonRes_clicked(self):
        self.handle_equals() 

    def handle_digit(self, digitchar):
        display = self.ui.display
        display.setText(self._display_txt() + digitchar)

    def handle_operator(self, opchar):
        display = self.ui.display
        if self._last_display_char_is_digit():
            display.setText(self._display_txt() + opchar)

    def handle_equals(self):
        display = self.ui.display
        if self._last_display_char_is_digit():
            self._compute_result()

    def keyPressEvent(self, event):
        key = str(event.text())
        if key.isdigit():
            self.handle_digit(key)
        elif key in ["+", "-", "*", "/"]:
            self.handle_operator(key)
        elif event.matches(QKeySequence.InsertParagraphSeparator):
            self.handle_equals()
        else:
            super(CalculatorDialog, self).keyPressEvent(event)
         

    def _display_txt(self):
        return str(self.ui.display.text())

    def _last_display_char_is_digit(self):
        txt = self._display_txt()
        return txt and txt[-1].isdigit()

    def _compute_result(self):
        res = eval(self._display_txt())
        self.ui.display.setText(str(res))
        


app = QApplication(sys.argv)
dialog = CalculatorDialog()
dialog.show()
sys.exit(app.exec_())
