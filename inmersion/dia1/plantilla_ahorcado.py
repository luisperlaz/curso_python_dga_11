# Modelo  sacado del curso:  A Gentle Introduction to Programming Using Python (MIT)
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/assignments/hangman_template.py



from random import randrange

# constantes
FICHERO_PALABRAS = "palabras.txt"
MAX_INTENTOS = 5


def carga_palabras(fichero):
    """
    Devuelve una lista de palabras válidas para el juego.
    Las palabras son cadenas de letras minúsculas. Las palabras dentro del
    fichero estás separadas por espacios en blanco.
    """

    print "Cargando palabras ..."
    # fin: fichero abierto para lectura
    fin = # escribe la instrucción

    lista_apalabras =  # lee la cadena y trocéala

    print "  ", len(lista_palabras), "palabras cargadas."
    # devuelve la lista

def dame_palabra(lista_palabras):
    """
    Selecciona una palabra al azar.

    *** Busca en el módulo random ...
    """

    pass

def adivina_palabra(letras, oculta):
    '''
    Devuelve True si el jugador ha acertado la palabra. Si no, devuelve falso.

    letras es una lista con las letras que ha introducido el jugador
    '''
    pass

def imprime_palabra(letras, oculta):
    '''
    Imprime las letras adivinadas. Las que no ha adivinado las imprime como
    un guión bajo.
    '''
    pass

def inicia_juego():
    # comienza el juego
    palabra_secreta = # llama a la función que devuelve una palabra al azar.
    letras_jugador = []
    errores = 0
    pass

def juega_de_nuevo():
    '''
    Pregunta si quiere jugar de nuevo una vez terminado el juego.

    Devuelve True / False
    '''
    pass

def pide_letra(letras):
    '''
    Pide una nueva letra al jugador. Si la letra no es válida (no es una
    letra) o ya la había introducido antes, vuelve a pedir una letra.

    Devuelve la letra que introduce el juegador
    '''

def muestra_tablero(letras, oculta, intentos):
    '''
    Muestra el estado del tablero: errores y letras adivinadas de la palabra
    oculta.
    Puedes mostrar en ascii un dibujo del ahorcado
    '''


# Bucle principal del juego
while True:
    # crea el esqueleto de acciones del juego.
    # Ayúdate del esquema gráfico.
    # Si es necesario puedes crear más funciones.
    pass
