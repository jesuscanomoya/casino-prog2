import pygame  # Importa la biblioteca Pygame, que es usada para crear videojuegos.
import sys  # Importa el módulo sys, que proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python.

from ajustes import *  # Importa todas las variables y funciones del módulo 'ajustes'.
from maquina import MaquinaBlackjack  # Importa la clase 'MaquinaBlackjack' del módulo 'maquina'.

class Juego:  # Define una clase llamada 'Juego'.
    def __init__(self):  # Define el método inicializador de la clase.
        pygame.init()  # Inicializa todos los módulos importados de Pygame.
        self.pantalla = pygame.display.set_mode((anchura, altura))  # Crea la ventana de juego con las dimensiones especificadas por 'anchura' y 'altura'.
        self.en_juego = False
        self.reloj = pygame.time.Clock()  # Crea un objeto de reloj que puede ser usado para controlar la velocidad de actualización del juego.
        #self.tiempo_delta = 0  # Inicializa la variable 'tiempo_delta' a 0.

        # Sonido
        # sonido_principal = pygame.mixer.Sound("Sonidos/Cancion principal.mp3")  # Carga el sonido principal del juego.
        # sonido_principal.play(loops=-1)  # Reproduce el sonido principal en un bucle infinito.

    def iniciar_juego(self):
        self.en_juego = True
        self.maquina = MaquinaBlackjack(self.pantalla)
        self.inicio()

    def terminar_juego(self):
        self.en_juego = False


    def inicio(self):  # Define el método 'inicio' de la clase.
        #self.tiempo_inicio = pygame.time.get_ticks()  # Obtiene el tiempo actual en milisegundos desde que se inicializó Pygame.

        while True:  # Comienza un bucle infinito.
            for event in pygame.event.get():  # Recorre todos los eventos que están en la cola de eventos de Pygame.
                if event.type == pygame.QUIT:  # Si el tipo de evento es 'QUIT' (que ocurre cuando el usuario cierra la ventana del juego)...
                    self.en_juego = False
                    print("aasdsd")

            #self.tiempo_delta = (pygame.time.get_ticks() - self.tiempo_inicio) / 1000  # Calcula el tiempo transcurrido desde el último frame en segundos.
            #self.tiempo_inicio = pygame.time.get_ticks()  # Actualiza el tiempo de inicio para el próximo frame.
            pygame.display.update()  # Actualiza la pantalla completa.
            self.pantalla.blit(self.imagen_fondo,(0, 0))  # Dibuja la imagen de fondo en la pantalla en la posición (0, 0).
            #while inicio:
            self.maquina.main_blackjack()
            #inicio = False
            self.reloj.tick(fps)  # Hace que el programa duerma el tiempo suficiente para mantener una velocidad de actualización constante especificada por 'fps'.

class Blackjack(Juego):  # Define una clase llamada 'Blackjack' que hereda de la clase 'Juego'.
    def __init__(self):  # Define el método inicializador de la clase.
        super().__init__()  # Llama al método inicializador de la clase padre 'Juego'.
        pygame.display.set_caption("Blackjack")  # Establece el título de la ventana del juego.
        self.imagen_fondo = pygame.image.load(fondo_blackjack)
        self.maquina = MaquinaBlackjack(self.pantalla)  # Crea una instancia de la clase 'MaquinaBlackjack'.

    def inicio_blackjack(self):  # Define el método 'inicio' de la clase.
        super().inicio()  # Llama al método 'inicio' de la clase padre 'Juego'.



if __name__ == "__main__":  # Si este módulo es el módulo principal (es decir, si no se ha importado desde otro módulo)...
    blackjack = Blackjack()  # Crea una instancia de la clase 'Blackjack'.
    blackjack.inicio()  # Llama al método 'inicio' de la instancia de 'Blackjack'.