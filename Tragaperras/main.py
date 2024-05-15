import pygame  # Importa la biblioteca Pygame, que es usada para crear videojuegos.
import sys  # Importa el módulo sys, que proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python.

from ajustes import *  # Importa todas las variables y funciones del módulo 'ajustes'.
from maquina import Maquina  # Importa la clase 'Maquina' del módulo 'maquina'.

class Juego:  # Define una clase llamada 'Juego'.
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

    def __init__(self):  # Define el método inicializador de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        pygame.init()  # Inicializa todos los módulos importados de Pygame.
        self.pantalla = pygame.display.set_mode(
            (anchura, altura))  # Crea la ventana de juego con las dimensiones especificadas por 'anchura' y 'altura'.
        self.reloj = pygame.time.Clock()  # Crea un objeto de reloj que puede ser usado para controlar la velocidad de actualización del juego.
        self.tiempo_delta = 0  # Inicializa la variable 'tiempo_delta' a 0.

        # Sonido
        sonido_principal = pygame.mixer.Sound("Sonidos/Cancion principal.mp3")  # Carga el sonido principal del juego.
        sonido_principal.set_volume(0.3)
        sonido_principal.play(loops=-1)  # Reproduce el sonido principal en un bucle infinito.

    def inicio(self):  # Define el método 'inicio' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        self.tiempo_inicio = pygame.time.get_ticks()  # Obtiene el tiempo actual en milisegundos desde que se inicializó Pygame.

        while True:  # Comienza un bucle infinito.
            for event in pygame.event.get():  # Recorre todos los eventos que están en la cola de eventos de Pygame.
                if event.type == pygame.QUIT:  # Si el tipo de evento es 'QUIT' (que ocurre cuando el usuario cierra la ventana del juego)...
                    pygame.quit()  # Cierra todos los módulos de Pygame.
                    sys.exit()  # Termina la ejecución del programa.

            self.tiempo_delta = (pygame.time.get_ticks() - self.tiempo_inicio) / 1000  # Calcula el tiempo transcurrido desde el último frame en segundos.
            self.tiempo_inicio = pygame.time.get_ticks()  # Actualiza el tiempo de inicio para el próximo frame.

            pygame.display.update()  # Actualiza la pantalla completa.
            self.pantalla.blit(self.imagen_fondo,
                               (0, 0))  # Dibuja la imagen de fondo en la pantalla en la posición (0, 0).
            self.maquina.actualizar(self.tiempo_delta)  # Actualiza la lógica de la máquina tragaperras.

            self.reloj.tick(
                fps)  # Hace que el programa duerma el tiempo suficiente para mantener una velocidad de actualización constante especificada por 'fps'.

class Tragaperras(Juego):  # Define una clase llamada 'Tragaperras' que hereda de la clase 'Juego'.
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

    def __init__(self):  # Define el método inicializador de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        super().__init__()  # Llama al método inicializador de la clase padre 'Juego'.
        self.imagen_fondo = pygame.image.load(fondo)  # Carga la imagen de fondo del juego.
        pygame.display.set_caption("Tragaperras")  # Establece el título de la ventana del juego.
        self.maquina = Maquina()  # Crea una instancia de la clase 'MaquinaTragaperras'.

    def inicio_tragaperras(self):  # Define el método 'inicio' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        super().inicio()  # Llama al método 'inicio' de la clase padre 'Juego'.

if __name__ == "__main__":  # Si este módulo es el módulo principal (es decir, si no se ha importado desde otro módulo)...
    tragaperras = Tragaperras()  # Crea una instancia de la clase 'Juego'.
    tragaperras.inicio()  # Llama al método 'inicio' de la instancia de 'Juego'.

