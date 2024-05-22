import pygame
import sys
from ajustes import *

class Interfaz:
    """
    Representa la interfaz de usuario del juego de Blackjack.

    Esta clase gestiona la creación y manipulación de elementos de la interfaz de usuario, como botones y áreas de la pantalla.

    Parameters
    ----------
    pantalla : pygame.Surface
        La superficie de Pygame donde se renderizará la interfaz.

    Attributes
    ----------
    button_pedir_carta_rect : pygame.Rect
        El rectángulo del botón 'Pedir Carta'.
    button_plantarse_rect : pygame.Rect
        El rectángulo del botón 'Plantarse'.
    button_jugar_rect : pygame.Rect
        El rectángulo del botón 'Jugar'.
    button_salir_rect : pygame.Rect
        El rectángulo del botón 'Salir'.
    button_apuesta1 : pygame.Rect
        El rectángulo del botón de apuesta de 1 ficha.
    button_apuesta5 : pygame.Rect
        El rectángulo del botón de apuesta de 5 fichas.
    button_apuesta10 : pygame.Rect
        El rectángulo del botón de apuesta de 10 fichas.
    button_apuesta25 : pygame.Rect
        El rectángulo del botón de apuesta de 25 fichas.
    button_apuesta50 : pygame.Rect
        El rectángulo del botón de apuesta de 50 fichas.
    button_apuesta100 : pygame.Rect
        El rectángulo del botón de apuesta de 100 fichas.
    button_confirmar : pygame.Rect
        El rectángulo del botón 'Confirmar'.

    pantalla : pygame.Surface
        La superficie de Pygame donde se renderiza la interfaz.
    """

    def __init__(self, pantalla):
        """
        Inicializa una nueva instancia de Interfaz.

        Parameters
        ----------
        pantalla : pygame.Surface
            La superficie de Pygame donde se renderizará la interfaz.
        """

        self.button_pedir_carta_rect = pygame.Rect(100, 300, 200, 50)
        self.button_plantarse_rect = pygame.Rect(100, 400, 200, 50)
        self.button_jugar_rect = pygame.Rect(300, 350, 400, 50)
        self.button_salir_rect = pygame.Rect(800, 350, 400, 50)
        self.pantalla = pantalla
        self.button_apuesta1 = pygame.Rect(500, 250, 200, 50)
        self.button_apuesta5 = pygame.Rect(500, 325, 200, 50)
        self.button_apuesta10 = pygame.Rect(500, 400, 200, 50)
        self.button_apuesta25 = pygame.Rect(800, 250, 200, 50)
        self.button_apuesta50 = pygame.Rect(800, 325, 200, 50)
        self.button_apuesta100 = pygame.Rect(800, 400, 200, 50)
        self.button_confirmar = pygame.Rect(650, 500, 200, 50)

    def draw_buttons(self):
        """
        Dibuja los botones "Pedir carta" y "Plantarse" en la interfaz de usuario.

        Utiliza la superficie de Pygame para dibujar los botones en las posiciones definidas por los atributos de la clase.
        Los botones tienen colores predefinidos y texto asociado que indica su función.
        """

        font = pygame.font.SysFont(None, 30)

        # Dibuja el botón "Pedir carta"
        pygame.draw.rect(self.pantalla, verde, self.button_pedir_carta_rect)
        text = font.render("Pedir carta", True, negro)
        self.pantalla.blit(text, (self.button_pedir_carta_rect.centerx - text.get_width() // 2,
                                  self.button_pedir_carta_rect.centery - text.get_height() // 2))

        # Dibuja el botón "Plantarse"
        pygame.draw.rect(self.pantalla, rojo, self.button_plantarse_rect)
        text = font.render("Plantarse", True, negro)
        self.pantalla.blit(text, (self.button_plantarse_rect.centerx - text.get_width() // 2,
                                  self.button_plantarse_rect.centery - text.get_height() // 2))


    def mostrar_puntos_crupier(self, puntos):
        """
        Muestra los puntos del crupier en la interfaz de usuario.

        Utiliza la superficie de Pygame para renderizar el texto que indica los puntos del crupier en la posición definida.

        Parameters
        ----------
        puntos : int
            La cantidad de puntos que tiene el crupier.
        """

        font = pygame.font.Font(None, 45)

        text = font.render('Crupier:', True, blanco)
        text_rect = text.get_rect(center=(400, 150))
        self.pantalla.blit(text, text_rect)

        text = font.render(f'{puntos}', True, blanco)
        text_rect = text.get_rect(center=(500, 150))
        self.pantalla.blit(text, text_rect)


    def mostrar_puntos_jugador(self, puntos):
        """
        Muestra los puntos del jugador en la interfaz de usuario.

        Utiliza la superficie de Pygame para renderizar el texto que indica los puntos del jugador en la posición definida.

        Parameters
        ----------
        puntos : int
            La cantidad de puntos que tiene el jugador.
        """

        font = pygame.font.Font(None, 45)

        text = font.render('Jugador:', True, blanco)
        text_rect = text.get_rect(center=(400, 650))
        self.pantalla.blit(text, text_rect)

        text = font.render(f'{puntos}', True, blanco)
        text_rect = text.get_rect(center=(500, 650))
        self.pantalla.blit(text, text_rect)

    def actualizar_puntuacion(self, puntos_crupier, puntos_jugador):
        """
        Actualiza la puntuación mostrada en la interfaz de usuario con los puntos del crupier y del jugador.

        Utiliza la superficie de Pygame para renderizar el texto que indica los puntos del crupier y del jugador en las posiciones definidas.

        Parameters
        ----------
        puntos_crupier : int
            La cantidad de puntos que tiene el crupier.
        puntos_jugador : int
            La cantidad de puntos que tiene el jugador.
        """

        font = pygame.font.Font(None, 45)

        text = font.render('Crupier:', True, blanco)
        text_rect = text.get_rect(center=(400, 150))
        self.pantalla.blit(text, text_rect)

        text = font.render(f'{puntos_crupier}', True, blanco)
        text_rect = text.get_rect(center=(500, 150))
        self.pantalla.blit(text, text_rect)

        text = font.render('Jugador:', True, blanco)
        text_rect = text.get_rect(center=(400, 650))
        self.pantalla.blit(text, text_rect)

        text = font.render(f'{puntos_jugador}', True, blanco)
        text_rect = text.get_rect(center=(500, 650))
        self.pantalla.blit(text, text_rect)

    def handle_events(self):
        """
        Maneja los eventos de la interfaz de usuario.

        Detecta eventos de ratón, como hacer clic, y verifica si el clic ocurre en los botones 'Pedir carta' o 'Plantarse'.
        Si se detecta un clic en uno de los botones, se devuelve la acción asociada al botón.

        Returns
        -------
        str or None
            La acción asociada al botón clickeado:
            - 'pedir_carta' si se hace clic en el botón 'Pedir carta'.
            - 'turno_crupier' si se hace clic en el botón 'Plantarse'.
            None si no se hace clic en ninguno de los botones.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button_pedir_carta_rect.collidepoint(mouse_pos):
                    return 'pedir_carta'
                if self.button_plantarse_rect.collidepoint(mouse_pos):
                    return 'turno_crupier'

    def mostrar_resultado(self, resultado):
        """
        Muestra el resultado del juego en la interfaz de usuario.

        Utiliza la superficie de Pygame para renderizar el texto que indica el resultado del juego en la posición definida.

        Parameters
        ----------
        resultado : str
            El resultado del juego, puede ser 'BLACKJACK', 'Has ganado', 'Has perdido' o 'Hay empate'.
        """

        font = pygame.font.Font(None, 45)
        text = font.render(resultado, True, blanco)
        text_rect = text.get_rect(center=(750, 275))
        self.pantalla.blit(text, text_rect)
        pygame.display.update()


    def draw_play(self):
        """
        Dibuja los botones 'Jugar' y 'Salir' en la interfaz de usuario.

        Utiliza la superficie de Pygame para dibujar los botones en las posiciones definidas por los atributos de la clase.
        Los botones tienen colores predefinidos y texto asociado que indica su función.
        """

        font = pygame.font.SysFont(None, 30)

        # Dibuja el botón "Volver a jugar"
        pygame.draw.rect(self.pantalla, blanco, self.button_jugar_rect)
        text = font.render("Jugar", True, negro)
        self.pantalla.blit(text, (self.button_jugar_rect.centerx - text.get_width() // 2,
                                  self.button_jugar_rect.centery - text.get_height() // 2))

        #Dibuja el botón "Salir"
        pygame.draw.rect(self.pantalla, blanco, self.button_salir_rect)
        text = font.render("Salir", True, negro)
        self.pantalla.blit(text, (self.button_salir_rect.centerx - text.get_width() // 2,
                                  self.button_salir_rect.centery - text.get_height() // 2))

        pygame.display.update()


    def handle_final_events(self):
        """
        Maneja los eventos finales de la interfaz de usuario.

        Detecta eventos de ratón, como hacer clic, y verifica si el clic ocurre en los botones 'Jugar' o 'Salir'.
        Si se detecta un clic en uno de los botones, se devuelve la acción asociada al botón.

        Returns
        -------
        str or None
            La acción asociada al botón clickeado:
            - 'jugar' si se hace clic en el botón 'Jugar'.
            - 'salir' si se hace clic en el botón 'Salir'.
            None si no se hace clic en ninguno de los botones.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button_jugar_rect.collidepoint(mouse_pos):
                    return 'jugar'
                if self.button_salir_rect.collidepoint(mouse_pos):
                    return 'salir'

    def limpiar_elementos(self, saldo):
        """
        Limpia la pantalla y muestra el saldo actual del jugador en la interfaz de usuario.

        Utiliza la superficie de Pygame para borrar todos los elementos de la pantalla,
        cargar el fondo del juego y mostrar el saldo actual del jugador en la posición definida.

        Parameters
        ----------
        saldo : int
            El saldo actual del jugador.
        """

        self.pantalla.fill(blanco)
        self.pantalla.blit(pygame.image.load(fondo_blackjack), (0, 0))
        self.mostrar_saldo(saldo)

        pygame.display.flip()


    def draw_apuesta(self):
        """
        Dibuja los botones de apuesta y el botón para confirmar la apuesta en la interfaz de usuario.

        Utiliza la superficie de Pygame para dibujar los botones de apuesta en las posiciones definidas por los atributos de la clase.
        Los botones tienen colores predefinidos y texto asociado que indica el valor de la apuesta.
        Además, muestra el texto "Tu apuesta:" en la posición definida.
        """

        font = pygame.font.SysFont(None, 30)

        # Dibuja el botón "Apuesta de 1€"
        pygame.draw.rect(self.pantalla, blanco, self.button_apuesta1)
        text = font.render("1 €", True, negro)
        self.pantalla.blit(text, (self.button_apuesta1.centerx - text.get_width() // 2,
                                      self.button_apuesta1.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 5€"
        pygame.draw.rect(self.pantalla, blanco, self.button_apuesta5)
        text = font.render("5 €", True, negro)
        self.pantalla.blit(text, (self.button_apuesta5.centerx - text.get_width() // 2,
                                  self.button_apuesta5.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 10€"
        pygame.draw.rect(self.pantalla, blanco, self.button_apuesta10)
        text = font.render("10 €", True, negro)
        self.pantalla.blit(text, (self.button_apuesta10.centerx - text.get_width() // 2,
                                  self.button_apuesta10.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 25€"
        pygame.draw.rect(self.pantalla, blanco, self.button_apuesta25)
        text = font.render("25 €", True, negro)
        self.pantalla.blit(text, (self.button_apuesta25.centerx - text.get_width() // 2,
                                  self.button_apuesta25.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 50€"
        pygame.draw.rect(self.pantalla, blanco, self.button_apuesta50)
        text = font.render("50 €", True, negro)
        self.pantalla.blit(text, (self.button_apuesta50.centerx - text.get_width() // 2,
                                  self.button_apuesta50.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 100€"
        pygame.draw.rect(self.pantalla, blanco, self.button_apuesta100)
        text = font.render("100 €", True, negro)
        self.pantalla.blit(text, (self.button_apuesta100.centerx - text.get_width() // 2,
                                  self.button_apuesta100.centery - text.get_height() // 2))

        # Dibuja el botón "Confirmar apuesta"
        pygame.draw.rect(self.pantalla, negro, self.button_confirmar)
        text = font.render("Confirmar apuesta", True, blanco)
        self.pantalla.blit(text, (self.button_confirmar.centerx - text.get_width() // 2,
                                  self.button_confirmar.centery - text.get_height() // 2))

        # Dibuja apuesta provisional
        font = pygame.font.Font(None, 45)
        text = font.render('Tu apuesta:', True, blanco)
        text_rect = text.get_rect(center=(750, 150))
        self.pantalla.blit(text, text_rect)

        pygame.display.update()

    def mostrar_apuesta(self, apuesta):
        """
        Dibuja una apuesta provisional en la pantalla.

        Args:
            apuesta (str): La descripción de la apuesta que se va a mostrar.
        """

        # Dibuja apuesta provisional
        font = pygame.font.Font(None, 45)
        text = font.render(f'{apuesta}', True, blanco)
        text_rect = text.get_rect(center=(750, 200))
        self.pantalla.blit(text, text_rect)

        pygame.display.update()

    def handle_apuestas(self):
        """
        Maneja los eventos relacionados con las apuestas en el juego.

        Returns:
            int or bool: El valor de la apuesta seleccionada o False si se confirma.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button_apuesta1.collidepoint(mouse_pos):
                    return 1
                if self.button_apuesta5.collidepoint(mouse_pos):
                    return 5
                if self.button_apuesta10.collidepoint(mouse_pos):
                    return 10
                if self.button_apuesta25.collidepoint(mouse_pos):
                    return 25
                if self.button_apuesta50.collidepoint(mouse_pos):
                    return 50
                if self.button_apuesta100.collidepoint(mouse_pos):
                    return 100
                if self.button_confirmar.collidepoint(mouse_pos):
                    return False

    def mostrar_saldo(self, saldo):
        """
        Muestra el saldo actual en la pantalla del juego.

        Args:
            saldo (float): El saldo actual del jugador.
        """

        font = pygame.font.Font(None, 45)
        text = font.render(f'Saldo actual: {saldo}', True, blanco)
        text_rect = text.get_rect(center=(150, 700))
        self.pantalla.blit(text, text_rect)

        pygame.display.update()