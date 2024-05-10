import random
from ajustes import *
import pygame
from interfaz import *

class MaquinaBlackjack:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.mano_jugador = []
        self.mano_crupier = []
        self.saldo = 10
        self.interfaz = Interfaz(pantalla, self.saldo)  # Creamos una instancia de la clase Interfaz
        self.pedir_carta_jugador = False
        self.carta_oculta = True

    def calcular_puntuacion(self, mano):  # Definimos la clase calcular_puntuación con el atributo 'mano'.
        puntuacion = 0  # Creamos la variable 'puntuación' y la inicializamos en 0, donde se irá actualizando la puntuación obtenida hasta el momento
        ases = 0  # Creamos la variable 'ases' y la inicializamos en 0, donde se irá actualizando los ases que vayan tocando.
        for carta in mano:  # Bucle for que itera sobre la lista 'mano' para inspeccionar cada carta.
            valor = carta[0]  # Damos a 'valor' el valor de 'carta[0]', el cual es el elemento de la lista de 'valores'.
            if valor == 'A':  # Condición si el valor es igual a 'A'.
                ases += 1  # Al ser 'A' un as, se suma 1 a la variable 'ases'.
                puntuacion += 11  # 'A' puede valer 1 o 11 pero le damos el valor inical de 11 y se lo sumamos a la variable 'puntuacion'.
            elif valor in ['J', 'Q', 'K']:  # Condición si el valor es igual a 'J', 'Q' o 'K'.
                puntuacion += 10  # Se suma 10 a la variable 'puntuacion'.
            else:  # Condición si no cumple ninguna de las previas (El valor es un número del 2 al 10).
                puntuacion += int(valor)  # Se suma su valor en forma de 'int' a la variable 'puntuacion'.

        while puntuacion > 21 and ases:  # Mientras que la variable 'puntuacion' supere 21 y la variable 'ases' != 0 se interpreta el as como 1 y no como 11.
            puntuacion -= 10  # Restamos 10 a la variable 'puntuacion' ya que hacemos que el as valga 1 y no 11.
            ases -= 1  # Restamos el as utilizado de 'ases'

        return puntuacion

    def pedir_carta(self, mano):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        palos = ['Corazones', 'Diamantes', 'Treboles', 'Picas']
        carta = (random.choice(valores), random.choice(palos))
        mano.append(carta)

        return mano


    def mostrar_mano(self):
        # Coordenadas iniciales para la mano del jugador
        x_jugador = 600
        y_jugador = 600

        # Coordenadas iniciales para la mano del crupier
        x_crupier = 600
        y_crupier = 100

        # Mostrar la mano del jugador
        for i, carta in enumerate(self.mano_jugador):
            imagen_carta = pygame.image.load(f"Proyecto/{carta[0]}_{carta[1]}.png")
            self.pantalla.blit(imagen_carta, (x_jugador + i * 100, y_jugador))

        # Mostrar la mano del crupier (ocultando la segunda carta)
        for i, carta in enumerate(self.mano_crupier):
            if i == 0 and self.carta_oculta:
                imagen_carta = pygame.image.load("Proyecto/carta_oculta1.png")  # Carta oculta del crupier
            else:
                imagen_carta = pygame.image.load(f"Proyecto/{carta[0]}_{carta[1]}.png")
            self.pantalla.blit(imagen_carta, (x_crupier + i * 100, y_crupier))

        pygame.display.update()

    def comparar_mano(self):
        puntuacion_jugador = self.calcular_puntuacion(self.mano_jugador)
        puntuacion_crupier = self.calcular_puntuacion(self.mano_crupier)

        if puntuacion_jugador == 21:
            resultado = 'BLACKJACK'
        elif puntuacion_jugador > 21:
            resultado = 'Has perdido'
        elif puntuacion_crupier > 21:
            resultado = 'Has ganado'
        elif puntuacion_jugador == puntuacion_crupier:
            resultado = 'Hay empate'
        elif puntuacion_jugador > puntuacion_crupier:
            resultado = 'Has ganado'
        else:
            resultado = 'Has perdido'

        return resultado


    def turno_jugador(self):
        seguir = True
        while seguir and self.calcular_puntuacion(self.mano_jugador) < 21:
            if self.pedir_carta_jugador:  # Solo pedir carta si el jugador ha pedido una
                self.pedir_carta(self.mano_jugador)
                self.mostrar_mano()
                self.pedir_carta_jugador = False  # Reiniciar el flag
            opcion = self.interfaz.handle_events()
            if opcion == 'pedir_carta':
                self.pedir_carta_jugador = True  # Marcar que el jugador ha pedido una carta
            elif opcion == 'turno_crupier':
                seguir = False



    def turno_crupier(self):
        decision = True
        while decision:
            self.carta_oculta = False
            self.mostrar_mano()
            puntos_crupier = self.calcular_puntuacion(self.mano_crupier)
            if puntos_crupier <= 16:
                self.pedir_carta(self.mano_crupier)
            else:
                decision = False


    def opcion_final(self):
        seguir = True
        while seguir:
            opcion = self.interfaz.handle_final_events()
            if opcion == 'jugar':
                seguir = False
            elif opcion == 'salir':
                seguir = False

        return opcion


    def gestion_apuesta(self):
        seguir = True
        apuesta = 0
        self.interfaz.mostrar_saldo()
        self.interfaz.draw_apuesta()
        self.interfaz.mostrar_apuesta(apuesta)
        while seguir:
            cantidad = self.interfaz.handle_apuestas()
            if cantidad == False:
                seguir = False
                self.interfaz.limpiar_elementos()
            elif cantidad in [1,5,10,25,50,100]:
                apuesta += cantidad
                self.interfaz.limpiar_elementos()
                self.interfaz.mostrar_saldo()
                self.interfaz.draw_apuesta()
                self.interfaz.mostrar_apuesta(apuesta)

        return apuesta



    def main_blackjack(self):
        juego = True
        while juego:
            apuesta = self.gestion_apuesta()
            self.interfaz.mostrar_saldo()
            self.interfaz.draw_buttons()
            for i in range(2):
                self.pedir_carta(self.mano_jugador)
                self.pedir_carta(self.mano_crupier)

            self.mostrar_mano()

            self.turno_jugador()
            if self.calcular_puntuacion(self.mano_jugador) < 21:
                self.turno_crupier()

            resultado = self.comparar_mano()

            self.interfaz.mostrar_resultado(resultado)

            if resultado == 'BLACKJACK':
                self.saldo += 2 * apuesta
            elif resultado == 'Has ganado':
                self.saldo += apuesta
            elif resultado == 'Has perdido':
                self.saldo -= apuesta

            self.interfaz.draw_play()

            opcion = self.opcion_final()
            if opcion == 'jugar':
                self.mano_crupier = []
                self.mano_jugador = []
                self.carta_oculta = True
                self.interfaz.limpiar_elementos()
            elif opcion == 'salir':
                juego = False