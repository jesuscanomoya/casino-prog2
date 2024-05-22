import pygame  # Importa la biblioteca Pygame, que es usada para crear videojuegos.
import sys  # Importa el módulo sys, que proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python.

from ajustes import *  # Importa todas las variables y funciones del módulo 'ajustes'.
from maquina2 import Maquina  # Importa la clase 'Maquina' del módulo 'maquina'.

from PyQt5 import QtCore, QtWidgets
from maquina import MaquinaBlackjack
from usuario import *
class Juego():  # Define una clase llamada 'Juego'.
    """
    Clase Juego: Gestiona la lógica principal del juego.

    Atributos
    ---------
    pantalla: pygame.Surface
        La superficie principal del juego donde se dibujan los elementos.
    reloj: pygame.time.Clock
        Un reloj para controlar la velocidad de actualización del juego.
    tiempo_delta: float
        El tiempo transcurrido desde la última actualización.

    Métodos
    -------
    inicio()
        Inicia el bucle principal del juego.
    """

    def __init__(self, jugador):  # Define el método inicializador de la clase.
        pygame.init()  # Inicializa todos los módulos importados de Pygame.

        self.reloj = pygame.time.Clock()  # Crea un objeto de reloj que puede ser usado para controlar la velocidad de actualización del juego.
        self.tiempo_delta = 0  # Inicializa la variable 'tiempo_delta' a 0.

        # Sonido
        sonido_principal = pygame.mixer.Sound("Tragaperras/Cancion principal.mp3")  # Carga el sonido principal del juego.
        sonido_principal.set_volume(0.3)
        sonido_principal.play(loops=-1)  # Reproduce el sonido principal en un bucle infinito.
        self.jugador = jugador
        self.juego_actual = None
        self.estado = 0

    def inicio(self):  # Define el método 'inicio' de la clase.
        self.tiempo_inicio = pygame.time.get_ticks()  # Obtiene el tiempo actual en milisegundos desde que se inicializó Pygame.

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if not self.running:  # Comprueba si 'self.running' es False
                    Usuario.actualizar_dinero(self.jugador.dni, self.jugador.balance)
                    pygame.quit()
                    break  # Si es así, rompe el bucle

            if not self.running:  # Comprueba si 'self.running' es False
                break

            self.tiempo_delta = (pygame.time.get_ticks() - self.tiempo_inicio) / 1000  # Calcula el tiempo transcurrido desde el último frame en segundos.
            self.tiempo_inicio = pygame.time.get_ticks()  # Actualiza el tiempo de inicio para el próximo frame.


            self.pantalla.fill((0, 0, 0))  # Llena la pantalla con color negro antes de dibujar.
            self.pantalla.blit(self.imagen_fondo, (0, 0))  # Dibuja la imagen de fondo en la pantalla en la posición (0, 0).


            if self.juego_actual == 'tragaperras':
                self.maquina.actualizar(self.tiempo_delta)
                pygame.display.flip()
            elif self.juego_actual == 'blackjack':
                self.maquinablackjack.main_blackjack()

            self.reloj.tick(fps)  # Hace que el programa duerma el tiempo suficiente para mantener una velocidad de actualización constante especificada por 'fps'.




class Tragaperras(Juego, QtWidgets.QWidget):  # Define una clase llamada 'Tragaperras' que hereda de la clase 'Juego'.
    """
    Clase Tragaperras: Gestiona la lógica específica del juego de tragaperras.

    Atributos
    ---------
    imagen_fondo : pygame.Surface
        La imagen de fondo del juego.
    maquina : Maquina
        Una instancia de la clase 'Maquina'.

    Métodos
    -------
    inicio_tragaperras()
        Inicia el bucle principal del juego de tragaperras.
    """

    def __init__(self,jugador, parent=None):  # Define el método inicializador de la clase.
        QtWidgets.QWidget.__init__(self, parent)
        Juego.__init__(self,jugador)  # Inicializa la parte de pygame
        self.pantalla = pygame.display.set_mode(
            (anchura_tragaperras, altura_tragaperras))  # Crea la ventana de juego con las dimensiones especificadas.
        self.setWindowTitle("Tragaperras")
        self.setGeometry(100, 100, 800, 600)
        self.imagen_fondo = pygame.image.load(fondo)  # Asegúrate de que el archivo "fondo.png" esté en el directorio correcto
        self.maquina = Maquina(self.jugador)

    def inicio_tragaperras(self):
        self.juego_actual = 'tragaperras'
        self.show()
        self.inicio()  # Llama al método inicio de la clase Juego

class Blackjack(Juego, QtWidgets.QWidget):  # Define una clase llamada 'Blackjack' que hereda de la clase 'Juego'.
    def __init__(self,jugador,  parent = None):  # Define el método inicializador de la clase.
        QtWidgets.QWidget.__init__(self, parent)
        Juego.__init__(self, jugador)  # Inicializa la parte de pygame.
        self.pantalla = pygame.display.set_mode(
            (anchura_blackjack, altura_blackjack))
        self.setWindowTitle("Blackjack")
        self.setGeometry(100, 100, 800, 600)
        self.imagen_fondo = pygame.image.load(fondo_blackjack)
        self.maquinablackjack = MaquinaBlackjack(self.pantalla, self.jugador)  # Crea una instancia de la clase 'MaquinaBlackjack'.


    def inicio_blackjack(self):
        self.juego_actual = 'blackjack'
        self.show()
        try:
            self.inicio()  # Llama al método inicio de la clase Juego
        except pygame.error:
            Usuario.actualizar_dinero(self.jugador.dni, self.jugador.balance)
            self.close()  # Cierra solo la ventana del juego de Blackjack
            pygame.quit()
            if self.estado == 0:
                pygame.quit()
                self.estado = 1
            else:
                self.inicio()









