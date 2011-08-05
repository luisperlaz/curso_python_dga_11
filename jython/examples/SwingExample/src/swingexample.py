'''
Ejemplo basico de Swing en Jython

@author: Luis Perez
'''
from javax.swing import *
from javax.swing import JButton #@UnresolvedImport
from javax.swing import JFrame #@UnresolvedImport

def hello(event):
    print "Hello. I'm an event."

def test_swing():
    frame = JFrame("Hello Jython")
    button = JButton("Pulsar", actionPerformed = hello)
    frame.add(button)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setSize(200, 100)
    frame.show()

if __name__ == "__main__":
    test_swing()