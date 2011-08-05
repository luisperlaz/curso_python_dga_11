import javax.swing as swing #@UnresolvedImport
import java #@UnresolvedImport
import operator

'''
@author: Luis Perez

Implementacion de una calculadora simple en swing para demostrar su uso desde jython

Es necesario completar el ejemplo para que la calculadora sea funcional con las operaciones
tipicas "/", "*", "-", "+", "=".
'''
class Calculator(swing.JFrame):
    
    operators_labels = ["/", "*", "-", "+", "="]
    
    def __init__(self):
        """"Constructor, creacion del JFrame y sus contenidos visuales"""
        swing.JFrame.__init__(self, size=(200, 300), title="Calculator") #@UndefinedVariable
        
        self.keyPressed = self.key_pressed

        self.contentPane.layout = java.awt.BorderLayout()
        self.contentPane.add(self.create_display(),
                java.awt.BorderLayout.NORTH)
        self.contentPane.add(self.create_digit_panel(), 
                java.awt.BorderLayout.WEST)

    def create_display(self):
        """Crea el panel del display"""
        panel = swing.JPanel(size=(200,100),
                border=swing.border.TitledBorder("Results"),
                layout=java.awt.BorderLayout(0, 10))
        self.display = swing.JTextField(preferredSize=(200,20),
                editable=0, background=(255, 255, 255),
                horizontalAlignment=swing.SwingConstants.RIGHT)
        self.display.text = ""
        panel.add(self.display, java.awt.BorderLayout.NORTH)
        return panel

    def create_digit_panel(self):
        """Crea el panel con los botones numericos"""
        box = swing.Box.createVerticalBox()
        box.add(self.create_digits_row((7, 8, 9)))
        box.add(self.create_digits_row((4, 5, 6)))
        box.add(self.create_digits_row((1, 2, 3)))
        box.add(self.create_digits_row((0,)))
        return box
    
    def create_digits_row(self, digits):
        """Crea una fila de botones numericos"""
        row = swing.Box.createHorizontalBox()
        for eachDigit in digits:
            if eachDigit != None:
                button = swing.JButton(str(eachDigit),
                        actionPerformed=self.digit_pressed)
                row.add(button)
        return row
    
    def create_operator_panel(self):
        """crea el panel de botones de operadores"""
        box = swing.Box.createVerticalBox()
        box.add(swing.JButton("CE", actionPerformed=self.clear_display))
        for operator in self.operators_labels:
            box.add(swing.JButton(operator, 
                    actionPerformed=self.operator_pressed))
        return box

    def digit_pressed(self, event):
        self.handle_digit(event.source.text)
        
    def key_pressed(self, event):
        char = event.keyChar
        # TODO
        event.consume()


if __name__ == "__main__":
    calc = Calculator()
    calc.show()
    
    #asociar globalmente un listener para la pulsacion de teclado
    kfm = java.awt.KeyboardFocusManager.getCurrentKeyboardFocusManager()
    class keystocalc(java.awt.KeyEventDispatcher):
        def dispatchKeyEvent(self,evt):
            if not evt.consumed and evt.ID == evt.KEY_PRESSED:
                calc.key_pressed(evt)
            return 0

    kfm.addKeyEventDispatcher(keystocalc())


