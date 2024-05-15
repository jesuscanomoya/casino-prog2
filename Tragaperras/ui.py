from jugador import Jugador  # Importa la clase 'Jugador' del módulo 'jugador'.
from ajustes import *  # Importa todas las variables y funciones del módulo 'ajustes'.
import pygame, random  # Importa los módulos 'pygame' y 'random'.

class UI:  # Define una clase llamada 'UI'.
    """
    Clase UI: Gestiona la interfaz de usuario del juego.

    Atributos
    ---------
    jugador : Jugador
        Una instancia de la clase 'Jugador'.
    display_surface : pygame.Surface
        La superficie actual de la pantalla.
    fuente : pygame.font.Font
        La fuente del texto de la interfaz de usuario.
    fuente_apuesta : pygame.font.Font
        La fuente del texto de la apuesta.
    win_fuente : pygame.font.Font
        La fuente del texto de victoria.
    win_angulo_texto : int
        El ángulo del texto de victoria.

    Métodos
    -------
    mostrar_info()
        Muestra la información del jugador en la pantalla.
    aumentar_apuesta()
        Aumenta la apuesta del jugador.
    diminuir_apuesta()
        Disminuye la apuesta del jugador.
    ajustar_apuesta()
        Ajusta la apuesta del jugador al balance del jugador.
    actualizar()
        Actualiza la interfaz de usuario.
    """

    def __init__(self, jugador):  # Define el método inicializador de la clase.
        """
        Parámetros
        ----------
        jugador : Jugador
            Una instancia de la clase 'Jugador'.
        """
        self.jugador = jugador
        self.display_surface = pygame.display.get_surface()
        self.fuente, self.fuente_apuesta = pygame.font.Font(ui_fuente, ui_tamaño_fuente), pygame.font.Font(ui_fuente,ui_tamaño_fuente)
        self.win_fuente = pygame.font.Font(ui_fuente, win_tamaño_fuente)
        self.win_angulo_texto = random.randint(-8,8)

    def mostrar_info(self):  # Define el método 'mostrar_info' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        datos_jugador = self.jugador.get_datos()

        # Balanace y tamño de apuesta
        balance_surface = self.fuente.render("Balance: €" + datos_jugador["balance"], True, color_texto, None)
        x, y = 20, self.display_surface.get_size()[1] - 30
        balance_rect = balance_surface.get_rect(bottomleft = (x, y))

        apuesta_surface = self.fuente_apuesta.render("Apuesta: " + datos_jugador["tamaño_apuesta"], True, color_texto, None)
        x = self.display_surface.get_size()[0] - 20
        apuesta_rect = apuesta_surface.get_rect(bottomright = (x, y))

        # Dibujar los datos del jugador
        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, apuesta_rect)
        self.display_surface.blit(balance_surface, balance_rect)
        self.display_surface.blit(apuesta_surface, apuesta_rect)

        # Print el ultimo win
        if self.jugador.ultimo_pago:
            ultimo_pago = datos_jugador["ultimo_pago"]
            win_surface = self.win_fuente.render("¡Has ganado! €" + ultimo_pago, True, color_texto, None)
            x1 = 800
            y1 = self.display_surface.get_size()[1] - 100
            win_surface = pygame.transform.rotate(win_surface, self.win_angulo_texto)
            win_rect = win_surface.get_rect(center = (x1, y1))
            self.display_surface.blit(win_surface, win_rect)

    def aumentar_apuesta(self):  # Define el método 'aumentar_apuesta' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        self.jugador.tamaño_apuesta += 10

    def diminuir_apuesta(self):  # Define el método 'diminuir_apuesta' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        self.jugador.tamaño_apuesta -= 10

    def ajustar_apuesta(self):  # Define el método 'ajustar_apuesta' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        self.jugador.tamaño_apuesta = self.jugador.balance

    def actualizar(self):  # Define el método 'actualizar' de la clase.
        """
        Parámetros
        ----------
        Ninguno
        """
        pygame.draw.rect(self.display_surface, "Black", pygame.Rect(0, 870, 1900, 300))
        pygame.draw.rect(self.display_surface, "Black", pygame.Rect(0, -240, 1900, 300))
        self.mostrar_info()







