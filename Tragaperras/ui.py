from jugador import Jugador
from ajustes import *
import pygame, random


class UI:
    def __init__(self, jugador):
        self.jugador = jugador
        self.display_surface = pygame.display.get_surface()
        self.fuente, self.fuente_apuesta = pygame.font.Font(ui_fuente, ui_tamaño_fuente), pygame.font.Font(ui_fuente,ui_tamaño_fuente)
        self.win_fuente = pygame.font.Font(ui_fuente, win_tamaño_fuente)
        self.win_angulo_texto = random.randint(-8,8)


    def mostrar_info(self):
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


    def actualizar(self):
        pygame.draw.rect(self.display_surface, "Black", pygame.Rect(0, 900, 1600, 100))
        self.mostrar_info()








