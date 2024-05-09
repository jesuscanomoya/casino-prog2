import pygame
import sys
from ajustes import *

class Interfaz:
    def __init__(self, pantalla):
        self.button_pedir_carta_rect = pygame.Rect(100, 300, 200, 50)
        self.button_plantarse_rect = pygame.Rect(100, 400, 200, 50)
        self.button_jugar_rect = pygame.Rect(300, 350, 400, 50)
        self.button_salir_rect = pygame.Rect(800, 350, 400, 50)
        self.pantalla = pantalla

    def draw_buttons(self):
        # Dibuja el botón "Pedir carta"
        pygame.draw.rect(self.pantalla, (0, 255, 0), self.button_pedir_carta_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Pedir carta", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_pedir_carta_rect.centerx - text.get_width() // 2,
                                  self.button_pedir_carta_rect.centery - text.get_height() // 2))

        # Dibuja el botón "Plantarse"
        pygame.draw.rect(self.pantalla, (255, 0, 0), self.button_plantarse_rect)
        text = font.render("Plantarse", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_plantarse_rect.centerx - text.get_width() // 2,
                                  self.button_plantarse_rect.centery - text.get_height() // 2))



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button_pedir_carta_rect.collidepoint(mouse_pos):
                    #self.pedir_carta()  # Llama a la función para pedir carta
                    return 'pedir_carta'
                if self.button_plantarse_rect.collidepoint(mouse_pos):
                    #self.plantarse()  # Llama a la función para plantarse
                    return 'turno_crupier'

    def mostrar_resultado(self, resultado):
        font = pygame.font.Font(None, 45)
        text = font.render(resultado, True, (255, 255, 255))
        text_rect = text.get_rect(center=(750, 275))
        self.pantalla.blit(text, text_rect)
        pygame.display.update()


    def draw_play(self):
        # Dibuja el botón "Volver a jugar"
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.button_jugar_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Jugar", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_jugar_rect.centerx - text.get_width() // 2,
                                  self.button_jugar_rect.centery - text.get_height() // 2))

        #Dibuja el botón "Salir"
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.button_salir_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Salir", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_salir_rect.centerx - text.get_width() // 2,
                                  self.button_salir_rect.centery - text.get_height() // 2))

        pygame.display.update()



    def handle_final_events(self):
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

    def limpiar_elementos(self):
        # Limpia la pantalla con el color del fondo
        self.pantalla.fill((255,255,255))
        self.pantalla.blit(pygame.image.load(fondo_blackjack), (0, 0))
        # Actualiza la pantalla
        pygame.display.flip()