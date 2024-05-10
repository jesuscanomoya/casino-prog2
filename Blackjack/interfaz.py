import pygame
import sys
from ajustes import *

class Interfaz:
    def __init__(self, pantalla, saldo):
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
        self.saldo = saldo

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

        font = pygame.font.Font(None, 45)
        text = font.render('Crupier', True, (255, 255, 255))
        text_rect = text.get_rect(center=(450, 150))
        self.pantalla.blit(text, text_rect)

        text = font.render('Jugador', True, (255, 255, 255))
        text_rect = text.get_rect(center=(450, 650))
        self.pantalla.blit(text, text_rect)



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


    def draw_apuesta(self):
        # Dibuja el botón "Apuesta de 1€"
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.button_apuesta1)
        font = pygame.font.SysFont(None, 30)
        text = font.render("1 €", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_apuesta1.centerx - text.get_width() // 2,
                                      self.button_apuesta1.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 5€"
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.button_apuesta5)
        font = pygame.font.SysFont(None, 30)
        text = font.render("5 €", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_apuesta5.centerx - text.get_width() // 2,
                                  self.button_apuesta5.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 10€"
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.button_apuesta10)
        font = pygame.font.SysFont(None, 30)
        text = font.render("10 €", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_apuesta10.centerx - text.get_width() // 2,
                                  self.button_apuesta10.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 25€"
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.button_apuesta25)
        font = pygame.font.SysFont(None, 30)
        text = font.render("25 €", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_apuesta25.centerx - text.get_width() // 2,
                                  self.button_apuesta25.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 50€"
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.button_apuesta50)
        font = pygame.font.SysFont(None, 30)
        text = font.render("50 €", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_apuesta50.centerx - text.get_width() // 2,
                                  self.button_apuesta50.centery - text.get_height() // 2))

        # Dibuja el botón "Apuesta de 100€"
        pygame.draw.rect(self.pantalla, (255, 255, 255), self.button_apuesta100)
        font = pygame.font.SysFont(None, 30)
        text = font.render("100 €", True, (0, 0, 0))
        self.pantalla.blit(text, (self.button_apuesta100.centerx - text.get_width() // 2,
                                  self.button_apuesta100.centery - text.get_height() // 2))

        # Dibuja el botón "Confirmar apuesta"
        pygame.draw.rect(self.pantalla, (0, 0, 0), self.button_confirmar)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Confirmar apuesta", True, (255, 255, 255))
        self.pantalla.blit(text, (self.button_confirmar.centerx - text.get_width() // 2,
                                  self.button_confirmar.centery - text.get_height() // 2))

        # Dibuja apuesta provisional
        font = pygame.font.Font(None, 45)
        text = font.render('Tu apuesta:', True, (255, 255, 255))
        text_rect = text.get_rect(center=(750, 150))
        self.pantalla.blit(text, text_rect)

        pygame.display.update()

    def mostrar_apuesta(self, apuesta):
        # Dibuja apuesta provisional
        font = pygame.font.Font(None, 45)
        text = font.render(f'{apuesta}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(750, 200))
        self.pantalla.blit(text, text_rect)

        pygame.display.update()

    def handle_apuestas(self):
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

    def mostrar_saldo(self):
        font = pygame.font.Font(None, 45)
        text = font.render(f'Saldo actual: {self.saldo}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(150, 700))
        self.pantalla.blit(text, text_rect)

        pygame.display.update()
